from abc import ABC, abstractmethod
import pygame


class AbstractSolution(ABC):
    def __init__(self, solution: any):
        self.__solution = solution

    @abstractmethod
    def verify(self, solution: "AbstractSolution") -> bool:
        '''
        Given a solution instance, compare if the solution is equal to self.
        '''

    @abstractmethod
    def draw(self, game: pygame):
        '''
        Given a pygame instance, draw the solution
        '''

    def get_solution(self):
        return self.__solution
