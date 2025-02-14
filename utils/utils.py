def manual_input(board, IA):
    while True:
        print("\nActions disponibles:")
        print("1. Placer une pièce" if  board.can_move_pieces else "2. Déplacer une pièce")
        print("3. Quitter")

        choix = input("Choisissez une action (1-3) : ")

        if choix == '1':
            try:
                i = int(input("Entrez la ligne (0-2) : "))
                j = int(input("Entrez la colonne (0-2) : "))
                board.place_piece(i, j)
                print(f"✅ Pièce placée en ({i}, {j})")
                print(board)

                # L'IA joue après le joueur
                best_move = IA.find_best_move(board)
                if best_move:
                    i1, j1, i2, j2 = best_move
                    board.make_move(i1, j1, i2, j2)
                    print(f"🤖 L'IA a joué : ({i1}, {j1}) -> ({i2}, {j2})")
                    print(board)
                else:
                    print("⚠️ Aucun coup possible pour l'IA.")

            except Exception as e:
                print(f"❌ Erreur : {e}")

        elif choix == '2':
            try:
                i1 = int(input("Entrez la ligne de départ (0-2) : "))
                j1 = int(input("Entrez la colonne de départ (0-2) : "))
                i2 = int(input("Entrez la ligne d'arrivée (0-2) : "))
                j2 = int(input("Entrez la colonne d'arrivée (0-2) : "))
                board.make_move(i1, j1, i2, j2)
                print(f"✅ Déplacement de ({i1}, {j1}) vers ({i2}, {j2})")
                print(board)

                # Coup de l'IA
                best_move = IA.find_best_move(board)
                if best_move:
                    i1, j1, i2, j2 = best_move
                    board.make_move(i1, j1, i2, j2)
                    print(f"🤖 L'IA a joué : ({i1}, {j1}) -> ({i2}, {j2})")
                    print(board)
                else:
                    print("⚠️ Aucun coup possible pour l'IA.")

            except Exception as e:
                print(f"❌ Erreur : {e}")

        elif choix == '3':
            print("👋 Fin de la partie. Au revoir !")
            break

        else:
            print("❌ Choix invalide. Veuillez entrer un chiffre entre 1 et 3.")
