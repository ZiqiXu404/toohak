from abc import ABC, abstractmethod
import pygame
from ... import AbstractSolution


class AbstractQuestion(ABC):
    def __init__(self, question: str, solution: AbstractSolution):
        self.__question = question
        self.__solution = solution

    @abstractmethod
    def verify(self, solution: AbstractSolution):
        '''
        Given a solution instance, verify if the solution is correct.
        '''

    @abstractmethod
    def draw(self, game: pygame):
        '''
        Given a pygame instance, represent the question on the canvas.
        '''

    def get_question(self):
        return self.__question

    def get_solution(self):
        return self.__solution
