import asyncio
import concurrent.futures._base
import traceback
from contextlib import suppress
from random import randint


#  TEALSTREET
class AsyncioSafeTasks():

    def __init__(self, *args, parent_task_manager=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._tasks = {}
        self._persistent_tasks = {}
        self.parent_task_manager = parent_task_manager


    def create_id(self):
        return randint(0, 100000)


    def create_task(self, awaitable, id=None, persistent=True, timeout=None, on_success=None, on_error=None, callback=None, print_exception=True):
        if self.parent_task_manager:
            return self.parent_task_manager.create_task(awaitable, id=id, persistent=persistent)
        id = id or self.create_id()
        def callback_helper(task):
            res = None
            try:
                with suppress(asyncio.CancelledError, concurrent.futures._base.CancelledError):
                    res = task.result()
            except Exception as e:
                try:
                    if callback:
                        callback(e)
                    handled_error = False
                    if on_error:
                        handled_error = True
                        on_error(e)
                    if hasattr(self, 'task_error_handler'):
                        handled_error = True
                        self.task_error_handler(e)
                    if not handled_error and print_exception:
                        traceback.print_exc()
                except Exception as e:
                    traceback.print_exc()
            try:
                if on_success:
                    on_success(res)
                if callback:
                    callback(res)
            except Exception as e:
                traceback.print_exc()
            try:
                if id in self._tasks:
                    self._tasks.pop(id)
                elif id in self._persistent_tasks:
                    self._persistent_tasks.pop(id)
            except Exception as e:
                pass
        task = asyncio.create_task(self._do_task(awaitable))
        if persistent:
            self._persistent_tasks[id] = task
        else:
            self._tasks[id] = task
        task.add_done_callback(callback_helper)
        if timeout:
            task._timeout_task = self.create_task(self.timeout_tasks([task], timeout, on_error=on_error))
        task._id = id
        return task

    async def _do_task(self, awaitable):
        return await awaitable


    async def cleanup_tasks(self, on_error=None):
        if self.parent_task_manager:
            return await self.parent_task_manager.cleanup_tasks()
        tasks = set(self._tasks.values())
        for task in tasks:
            try:
                task.cancel()
                with suppress(asyncio.CancelledError, concurrent.futures._base.CancelledError):
                    await task
            except Exception as e:
                if on_error:
                    on_error(e)
        self._tasks = {}

    async def cancel_task(self, id, on_error=None):
        if self.parent_task_manager:
            return await self.parent_task_manager.cancel_task(id)
        found_task = None
        if id in self._tasks:
            found_task = self._tasks.pop(id)
        elif id in self._persistent_tasks:
            found_task = self._persistent_tasks.pop(id)

        if found_task:
            try:
                found_task.cancel()
                with suppress(asyncio.CancelledError, concurrent.futures._base.CancelledError):
                    await found_task
            except Exception as e:
                if on_error:
                    on_error(e)

    async def timeout_tasks(self, tasks, timeout, on_error=None):
        async def cancel_pending_tasks():
            await asyncio.sleep(timeout)
            if isinstance(tasks, list):
                for task in tasks:
                    if not task.done():
                        id = task._id
                        await self.cancel_task(id)
            else:
                for id, task in tasks.items():
                    if not task.done():
                        await self.cancel_task(id)

        id = self.create_id()
        # noinspection PyAsyncCall
        self.create_task(cancel_pending_tasks(), id=id)
        if isinstance(tasks, list):
            res = await asyncio.gather(*tasks)
        else:
            res = await asyncio.gather(*tasks.values())
        await self.cancel_task(id, on_error=on_error)
        return res

def asyncio_safe(cleanup=None):
    def async_safe_warpper(function):
        async def decorated(*args, **kwargs):
            try:
                return await function(*args, **kwargs)
            except concurrent.futures._base.CancelledError as e:
                cleanup and cleanup(*args, **kwargs)
                return
            except Exception as e:
                traceback.print_exc()
                cleanup and cleanup(*args, **kwargs)
                return
        return decorated
    return async_safe_warpper


