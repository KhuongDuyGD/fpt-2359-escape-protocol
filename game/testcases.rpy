# Engine-level smoke tests for the two complete branches. Run with:
#   renpy.py <project-directory> test good_route
#   renpy.py <project-directory> test bad_route

testcase good_route:
    run Jump("start")
    advance until screen "choice"
    click "Dậy ngay."
    advance until screen "choice"
    click "Bình tĩnh đọc đề."
    advance until screen "choice"
    click "Đi ăn."
    advance until screen "choice"
    click "Fix project ngay."
    advance until screen "choice"
    click "Ăn đàng hoàng."
    advance until screen "choice"
    click "Dùng laptop cá nhân."
    advance until screen "choice"
    click "ĐI VỀ."
    advance until screen "ending_card"
    assert eval (escaped_school and persistent.good_ending_unlocked and escape_point >= 4)
    click "Continue"
    assert screen "post_ending_actions"
    click "Start New Game+"
    advance until screen "choice"
    assert eval (energy == 100 and pending_tasks == 0 and not escaped_school)


testcase bad_route:
    run Jump("start")
    advance until screen "choice"
    click "Dậy ngay."
    advance until screen "choice"
    click "Bình tĩnh đọc đề."
    advance until screen "choice"
    click "Đi ăn."
    advance until screen "choice"
    click "Fix project ngay."
    advance until screen "choice"
    click "Ăn đàng hoàng."
    advance until screen "choice"
    click "Dùng laptop cá nhân."
    advance until screen "choice"
    click "“Ở lại một chút.”"
    advance until screen "ending_card"
    assert eval (not escaped_school and persistent.bad_ending_unlocked and assignment_uploaded)
    click "Continue"
    advance until screen "post_ending_actions"
    assert screen "post_ending_actions"


testcase ui_screens:
    run Jump("start")
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
