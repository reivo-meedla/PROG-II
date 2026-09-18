from enum import Enum
from abc import ABC, abstractmethod


class Person:
    def __init__(self, name):
        self.name = name


class Relationship(Enum):
    PARENT = 1
    CHILD = 2
    SIBLING = 3


class RelationshipBrowser(ABC):
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for person1, rel, person2 in self.relations:
            if person1.name == name and rel == Relationship.PARENT:
                yield person2.name


class Research:
    def __init__(self, browser):
        for child_name in browser.find_all_children_of("John"):
            print(f"John has a child called {child_name}")


parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)