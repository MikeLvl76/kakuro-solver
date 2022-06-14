from math import exp
from random import random

class Solution:

    def __init__(self, cooling_factor, iterations, temperature, Nt):
        self.COOLING_FACTOR = cooling_factor
        self.MAX_ITERATIONS = iterations
        self.temperature = temperature
        self.Nt = Nt

    def accept(self, difference, t):
        if difference >= 0:
            a = exp(-difference / t)
            return not random() >= a
        return True

    def increase_temperature(self, t):
        return t + (t - t * self.COOLING_FACTOR)

    def coolen(self, t):
        return t * self.COOLING_FACTOR

    def resolve(self, resolver):
        resolver.prepare()
        print("Resolving...")
        try:
            quality = resolver.get_quality()
            counter = 0
            step = 0
            temperature = self.temperature
            # While solution not found and iteration number hasn't reached its max
            while quality > 0 and step < self.MAX_ITERATIONS:
                # Calculates difference between actual and neighbor fitness n times
                # and update grid when its possible
                for _ in range(self.Nt):
                    resolver2 = resolver.neighbor()
                    difference = resolver2.get_quality() - resolver.get_quality()
                    # Change grid only if exp(-difference/temperature) > random(0, 1)
                    if self.accept(difference, temperature):
                        resolver = resolver2
            
                # Prevent to being stuck on the same quality and reach local minimum
                if quality != resolver.get_quality():
                    quality = resolver.get_quality()
                    counter = 0
                else:
                    counter += 1
                
                # Local minimum reached so we increase the temperature to quit this state
                if counter > 10:
                    temperature = self.increase_temperature(temperature)
                    counter = 0

                # Increase counter and lower temperature
                step += 1
                temperature = self.coolen(temperature)
        except Exception as e:
            print(e)

        return resolver