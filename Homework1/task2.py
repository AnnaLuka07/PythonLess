# Напишите программу для проверки ложности утверждения

# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.


print('X Y W Z')
for X in range(2):
    for Y in range(2):
        for W in range(2):
            for Z in range(2):
                if not ((W and Z) or not(Y) or not(X == W)): 
                    print(X, Y, W, Z ) 

