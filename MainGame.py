import PeopleFunc as PF
import People as P
import Actions as A


MainChar = PF.create_player()
MainVillain = PF.create_villain()
for i in range(3):
    P.enemy_list[i] = PF.create_bad_goon()
doc1 = PF.create_doctor()
doc2 = PF.create_doctor()
doc3 = PF.create_doctor()
P.enemy_list.append(MainVillain)
battle_counter = 0

for i in range(len(P.enemy_list)):
    print(P.enemy_list[i].get_name())

while len(P.enemy_list) > 0:
    A.battle_state(MainChar, A.enemy_select(P.enemy_list))
    if not MainChar.get_is_alive():
        print(f"\nYou survived {battle_counter} battle(s)!")
        break
    else:
        A.heal_check(MainChar, doc1)
    battle_counter += 1
    print(f"Congratulations! there are {len(P.enemy_list)} enemies left!\n")

    for i in range(len(P.enemy_list)):
                print(P.enemy_list[i].get_name())
                while len(P.enemy_list) > 0:
                    A.battle_state(MainChar, A.enemy_select(P.enemy_list))
                if not MainChar.get_is_alive():
                    print(f"\nYou survived {battle_counter} battle(s)!")
                    break
                else:
                    A.heal_check(MainChar, doc1)
                battle_counter += 1
                print(f"Congratulations! there are {len(P.enemy_list)} enemies left!\n")


