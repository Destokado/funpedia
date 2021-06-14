

#duel_trigger_winner = "CREATE TRIGGER check_winner_after_update" \
#                      "AFTER UPDATE ON duels WHEN old.challenger_counter >= old.goal OR old.rival_counter >= old.goal" \
#                      "BEGIN " \
#                      "INSERT INTO duels"
