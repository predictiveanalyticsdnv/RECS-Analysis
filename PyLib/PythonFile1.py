import numpy as np
import pandas as pd


def longFunc(inputNum):
	step1 = np.square(inputNum)
	step2 = step1 + 10
	step3 = step2 * 5
	step4 = round(np.sqrt(step3),2)

	return step4