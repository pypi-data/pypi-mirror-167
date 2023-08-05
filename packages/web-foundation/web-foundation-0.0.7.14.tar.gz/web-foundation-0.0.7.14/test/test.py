# from __future__ import annotations
#
# from abc import ABC
# from typing import Generic, TypeVar, Type
#
# from web_foundation.utils.helpers import in_obj_subclasses, in_obj_classes
#
#
# class Descriptor(ABC):
#
#     def __getattribute__(self, item):
#         pass
#
#     def __setattr__(self, key, value):
#         pass
#
#     def __delattr__(self, item):
#         pass
#
#
# class Service():
#     tt: str
#
#     def __init__(self, tt):
#         self.tt = tt
#
#     async def initasasg(self):
#         pass
#
#
# class YYYService(Service):
#     pass
#
#
# T = TypeVar("T")
#
#
# class Dependency(Generic[T]):  # type: ignore
#     _initialized: T | None = None
#     default: T | None
#     instance_of: Type[T] | None
#
#     def __init__(self, instance_of: Type[T] = None, default: T = None):
#         self.instance_of = instance_of
#         self.default = default
#
#     def __call__(self, *args, **kwargs) -> T:
#         if not self._initialized and not self.default:
#             raise AttributeError("Dependency must me initialized with from_initialized() or with default kwarg ")
#         if not self._initialized:
#             return self.default
#         return self._initialized
#
#     def from_initialized(self, obj) -> Dependency[T]:
#         if not isinstance(obj, self.instance_of) or not issubclass(obj.__class__, self.instance_of):
#             raise AttributeError("Dependency must init with same instance as instance_of or nested cls")
#         self._initialized = obj
#         return self
#
#
# class TestContainer:
#     ticket_service = Dependency(instance_of=Service, default=Service(22))
#
#     def __init__(self, **kwargs):
#         for dep, name in in_obj_classes(self, Dependency):
#             dep_init = kwargs.get(name)
#             if dep_init:
#                 dep.from_initialized(dep_init)
#
#         # if not dep_init and dep.default:
#         #     dep()
#         # if not dep_init or not dep.default:
#         #     raise AttributeError("Dependency must me initialized")
#         # elif dep.instance_of != type(dep_init) and not issubclass(type(dep_init), dep.instance_of):
#         #     raise AttributeError("Dependency must init with same instance as instance_of or nested cls")
#         # dep.from_initialized(dep_init)
#
#
# class NEwCOntainer(TestContainer):
#     some_service = Dependency(instance_of=Service)
#
#
# if __name__ == '__main__':
#     service = YYYService("asf")
#     t = NEwCOntainer(ticket_service=service)
#     q = t.some_service()
#     print(q)

class Test():
    pass


class Sub():
    test: Test

    def __init__(self, test: Test):
        self.test = test


class Container():
    t = Test()
    s = Sub(t)


c = Container()
print(c.s.test)
c.t = Test()
print(c.s.test)
