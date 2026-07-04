import unittest
from dataclasses import dataclass

from smartdisplayserverkit.utils.singleton import SingletonAsync


class SingletonTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_singleton(self):
        @dataclass(slots=True, frozen=True)
        class Database(SingletonAsync):
            age: int

            @classmethod
            async def init(cls, age: int) -> None:
                instance = cls(age)
                await super()._set_instance(instance)

        await Database.init(10)
        db1 = Database.instance()
        db2 = Database.instance()
        self.assertIs(db1, db2)
        self.assertEqual(db1.age, db2.age)
        self.assertEqual(db2.age, 10)
