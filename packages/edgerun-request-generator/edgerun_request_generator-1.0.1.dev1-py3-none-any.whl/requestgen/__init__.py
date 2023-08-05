import math
import pickle
import random
import time

import numpy as np
import pandas as pd
import simpy

__all__ = [
    'constant_rps_profile',
    'sine_rps_profile',
    'randomwalk_rps_profile',
    'static_arrival_profile',
    'expovariate_arrival_profile',
    'run_arrival_profile',
    'save_requests',
    'pre_recorded_profile',
    'concatenate_profiles_and_save'
]


def constant_rps_profile(rps):
    while True:
        yield rps


def run_rps_profile(env, profile, until, time_step=0.5):
    x = list()
    y = list()

    def generate_profile_data():
        while True:
            rps = next(profile)
            x.append(env.now)
            y.append(rps)
            yield env.timeout(time_step)

    env.process(generate_profile_data())
    env.run(until=until)

    return x, y


def sine_rps_profile(env, max_rps, period):
    """
    Generator that yields values according to a sine function where x = env.now, the y values are between 0 and max_rps,
    and the period between peaks is defined in seconds.

    :param env: the simulation environment
    :param max_rps: the peak of the sine wave
    :param period: the time in seconds between peaks
    """
    div = period / (2 * np.pi)  # divisor for stretching the period

    x = 0
    y = -1

    while True:
        if env.now == x and y >= 0:
            # return value from last calculation if time hasn't progressed
            yield y

        x = env.now
        y = math.sin(x / div)

        # scale y to RPS
        y = (y + 1) / 2
        y = y * max_rps

        yield y


def randomwalk_rps_profile(mu, sigma, max_rps, min_rps=0):
    """
    creates a random walk pattern with
    a start rps value (mu),
    standard deviation value (sigma), walk will be spikier with higher value,
    and max_rps which is the rps cap at where sampled values will be rejected
    :param mu: start rps value
    :param sigma: standard deviation value
    :param max_rps: rps cap
    :param min_rps: rps minimum
    :return: interarrival time generator
    """
    while True:
        nmu = random.normalvariate(mu, sigma)

        # reject out of bounds values
        if nmu >= max_rps:
            yield max_rps
        elif nmu <= min_rps:
            yield min_rps
        else:
            yield nmu
            mu = nmu


def static_arrival_profile(rps_generator, max_ia=math.inf):
    while True:
        rps = next(rps_generator)
        if rps == 0:
            yield max_ia

        ia = 1 / rps
        yield min(ia, max_ia)


def expovariate_arrival_profile(rps_generator, scale=1.0, max_ia=math.inf):
    while True:
        lam = next(rps_generator)
        ia = random.expovariate(lam) if lam > 0 else 1
        yield min(ia * scale, max_ia)


def pre_recorded_profile(file: str):
    with open(file, 'rb') as fd:
        yield from pickle.load(fd)


def run_arrival_profile(env, ia_gen, until):
    x = list()
    y = list()

    def event_generator():
        while True:
            ia = next(ia_gen)
            x.append(env.now)
            y.append(ia)
            yield env.timeout(ia)

    then = time.time()
    env.process(event_generator())
    env.run(until=until)
    print('simulating %d events took %.2f sec' % (len(x), time.time() - then))

    df = pd.DataFrame(data={'simtime': x, 'ia': y}, index=pd.DatetimeIndex(pd.to_datetime(x, unit='s', origin='unix')))
    return df


def save_requests(profile, duration, file: str, env: simpy.Environment = None):
    """
    Runs the profile and saves the generated interarrival times as pkl.
    :param profile: profile to run
    :param duration: the duration to run the profile, in seconds
    :param file: full file name
    :param env: environment to run the profile, if None creates a default simpy Environment
    """
    if env is None:
        env = simpy.Environment()
    with open(file, 'wb') as fd:
        df = run_arrival_profile(env, profile(env), until=duration)
        ias = list(df['ia'])
        pickle.dump(ias, fd)


def concatenate_profiles_and_save(file: str, profiles):
    env = simpy.Environment()
    dfs = []
    until = 0
    for profile, duration in profiles:
        until += duration
        df = run_arrival_profile(env, profile(env), until=until)
        dfs.append(df)

    ias = list(pd.concat(dfs)['ia'])
    with open(file, 'wb+') as fd:
        pickle.dump(ias, fd)
