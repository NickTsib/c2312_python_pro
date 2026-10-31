import warnings

warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("error", ImportWarning)

warnings.warn("Warnings, no code here", SyntaxWarning)
try:
    warnings.warn("Warnings, module not import", ImportWarning)
except:
    print("Warning processed")

