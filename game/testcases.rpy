# Engine-level smoke tests for the two complete branches. Run with:
#   renpy.py <project-directory> test good_route
#   renpy.py <project-directory> test bad_route

testcase good_route:
    run Jump("start")
    advance until screen "choice"
    click "Dậy. Ngay."
    advance until screen "choice"
    click "Đọc đề trước khi hoảng."
    advance until screen "choice"
    click "Đi ăn trước."
    advance until screen "choice"
    click "Fix luôn."
    advance until screen "choice"
    click "Ăn như một con người bình thường."
    advance until screen "choice"
    click "Rút laptop cá nhân."
    advance until screen "choice"
    click "Về."
    advance until screen "ending_card"
    assert eval (escaped_school and persistent.good_ending_unlocked and escape_point >= 4 and final_choice == 'leave')
    click "Continue"
    assert screen "post_ending_actions"
    click "Start New Game+"
    advance until screen "choice"
    assert eval (energy == 100 and pending_tasks == 0 and not escaped_school)


testcase bad_route:
    run Jump("start")
    advance until screen "choice"
    click "Dậy. Ngay."
    advance until screen "choice"
    click "Đọc đề trước khi hoảng."
    advance until screen "choice"
    click "Đi ăn trước."
    advance until screen "choice"
    click "Fix luôn."
    advance until screen "choice"
    click "Ăn như một con người bình thường."
    advance until screen "choice"
    click "Rút laptop cá nhân."
    advance until screen "choice"
    click "Ở lại thêm chút."
    advance until screen "ending_card"
    assert eval (not escaped_school and persistent.bad_ending_unlocked and assignment_uploaded and final_choice == 'stay')
    click "Continue"
    advance until screen "post_ending_actions"
    assert screen "post_ending_actions"


testcase failed_escape:
    # Leaving without enough Escape Points still reaches the night route.
    run Jump("start")
    advance until screen "choice"
    click "Năm phút nữa thôi."
    advance until screen "choice"
    click "Panic trước, đọc đề sau."
    advance until screen "choice"
    click "Join meeting."
    advance until screen "choice"
    click "Để chiều."
    advance until screen "choice"
    click "Vừa ăn vừa code."
    advance until screen "choice"
    click "Chờ."
    advance until screen "choice"
    click "Về."
    advance until screen "ending_card"
    assert eval (final_choice == 'leave' and not escaped_school and persistent.bad_ending_unlocked)


testcase ui_screens:
    run Jump("start")
    assert eval (active_speaker_image("PLAYER") == "player exhausted" and active_speaker_image("MINH") == "minh" and active_speaker_image(None) is None)
    run ShowMenu("save")
    assert screen "save"
    run ShowMenu("load")
    assert screen "load"
    run ShowMenu("preferences")
    assert screen "preferences"
    run ShowMenu("history")
    assert screen "history"
    run ShowMenu("ending_gallery")
    assert screen "ending_gallery"
