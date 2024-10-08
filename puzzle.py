from logic import *
import pdb

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

knowledge_base = And(
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    Or(CKnave, CKnight),
    Not(And(AKnave, AKnight)),
    Not(And(BKnave, BKnight)),
    Not(And(CKnave, CKnight))
)

# Puzzle 0
# A says "I am both a knight and a knave."

# cannot be both a knight and a knave, must be one or the other but not both. exclusive or.
# Every sentence spoken by a knight is true
# Every sentence spoken by a knave is false.

knowledge0 = And(

    knowledge_base,

    # A knight always speaks the truth. When a knight says they're a knight, they are not a knave
    Implication(AKnight, Not(AKnave)),

    # A knave could say it's a knight, when really it's a knave
    Implication(AKnight, AKnave)

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    knowledge_base,

    # this is what the knight would say, if this sentence was true (which it can't be)
    Implication(AKnight, And(AKnave, BKnave)),

    # what a knave would say-the lie-that they are not both knaves.
    Implication(AKnave, Not(And(AKnave, BKnave)))

    # result: A is a knave, B is a knight. A is a knave as it's lying (two A cannot be both knaves)
    # B is a knight because of the second implication. When A says not AKnave and not BKnave, and that's a lie
    # we can determine that B is a knight.
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    knowledge_base,
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Implication(BKnight, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Implication(BKnave, Or(And(AKnave, BKnave), And(AKnight, BKnight)))
)

# We know one of these (A or B) must be different because one is telling a lie.
# They can't be the same and different.

# Say A is a knight and says we are of the same kind, then B must also be a knight.
# But if B is a knight, then A must be a knave, since B is saying they must be different kinds.
# So this means A must be a knave, B is a knight.

# Try opposing: say A is a knave. this must be that B is a knight, since A is lying.
# Then B must be a knight, as what B says 'we are different kinds' is true.

# Bknight, Aknave

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO

    knowledge_base,
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),

    # If B is a knight, then it is possible that if A is a knight, it said it is a knave. or that A is a knave and it said it is not a knave. 
    # if B is a knave, then it is possible that A did not say anything-that NOT if A is a knight, it said it is a knave and NOT if A is a knave, it said it is not a knave
    Or(Implication(BKnight, Or(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))), 
        Implication(BKnave, Not(Or(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))))),

    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)

# if B is a knight->A must have said they are a knave and C is a knave.
# If C is a knave, A cannot be a knight, must be a knave.
# But then the sentence A is a knight or a knave would have to be false. which isn't true, as it must be either a knight or knave.

# so A must be a knight.
# which means B is lying-it must be a knave
# which means C is a knight since B said it was a knave.

# a knight
# b knave
# c knight


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]

    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                # pdb.set_trace()
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
