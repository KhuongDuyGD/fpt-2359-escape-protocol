# Main screenplay. Each scene is a label so student developers can reorder or
# expand one part of the day without touching the UI or ending logic.

label start:
    # Reset explicitly so the New Game+ jump starts from the same baseline.
    $ energy = 100
    $ sanity = 100
    $ academic_progress = 0
    $ escape_point = 0
    $ pending_tasks = 0
    $ attendance_done = False
    $ quiz_done = False
    $ group_task_done = False
    $ assignment_uploaded = False
    $ escaped_school = False

    show screen stats_hud
    if new_game_plus:
        centered "NEW GAME+\nDifficulty Unlocked: SENIOR YEAR."
        $ new_game_plus = False

    jump scene_00_alarm


label scene_00_alarm:
    scene bedroom_morning with fade
    show player at center with dissolve
    centered "06:29 AM"
    n "Ngày 25 tháng 9."
    n "Một ngày thứ Sáu tuyệt đẹp."
    n "Chim đang hót."
    n "Mặt trời đang mọc."
    n "Và cách đây khoảng tám tiếng..."
    n "PLAYER đã phạm một sai lầm chiến lược nghiêm trọng."
    p "..."
    p "Chơi thêm một trận thôi."
    scene bedroom_gaming with flash
    centered "02:47 AM"
    show player at center
    p "Ok trận cuối thật."
    scene bedroom_morning with fade
    centered "06:30 AM"
    play sound sfx_alarm
    centered "RRRRRRRRRRRRRR!!!!"
    show player at center with hpunch
    p "AAAAAAAA—"
    n "Boss đầu tiên xuất hiện."
    play sound sfx_boss
    call screen boss_title("THE ALARM CLOCK", "HP: ∞    •    Weakness: Không có.")

    menu:
        "Tắt báo thức và ngủ tiếp 5 phút.":
            $ energy += 10
            $ sanity += 5
            centered "07:18 AM"
            p "..."
            p "..."
            p "..."
            p "OH SH—"
            $ energy -= 20
            $ escape_point -= 1
        "Dậy ngay.":
            p "Không."
            p "Hôm nay tao sẽ sống như một con người có trách nhiệm."
            n "Một câu nói cực kỳ mạnh mẽ."
            n "Không ai trong căn phòng tin nó."
            $ escape_point += 1

    jump scene_01_gate


label scene_01_gate:
    scene school_gate with fade
    show player at left with dissolve
    centered "07:28 AM — CỔNG TRƯỜNG"
    p "CÒN HAI PHÚT!"
    n "Trong lịch sử nhân loại..."
    n "Usain Bolt từng đạt gần 45 km/h."
    n "Nhưng Usain Bolt chưa từng có tiết học lúc 7:30."
    n "PLAYER lao vào thang máy."
    n "Cửa chuẩn bị đóng."
    n "Một bàn tay chặn lại."
    show minh at right with dissolve
    m "Ê."
    p "Đừng."
    m "Tui chưa nói gì mà?"
    p "Tôi cảm nhận được deadline."
    m "Ông làm bài chưa?"
    p "..."
    m "À."
    p "Đừng nhìn tôi bằng ánh mắt đó."
    play sound sfx_bell
    centered "DING. 07:30."
    $ attendance_done = True
    jump scene_02_quiz


label scene_02_quiz:
    scene classroom with dissolve
    show player at left
    show minh at right
    show thaydev at center with dissolve
    dev "Good morning class."
    crowd "..."
    dev "Hôm nay chúng ta sẽ bắt đầu bằng một bài quiz nhỏ."
    stop music fadeout 0.2
    with flash
    p "..."
    m "..."
    student "Thầy ơi em xin về."
    dev "Quiz chỉ có 10 câu thôi."
    n "Tình hình tạm thời ổn định."
    dev "Open book."
    n "Cả lớp thở phào."
    dev "20 phút."
    p "Nice."
    dev "Có coding."
    with hpunch
    p "..."
    m "Chúng ta đã có một cuộc đời đẹp."

    menu:
        "Bình tĩnh đọc đề.":
            $ sanity -= 5
            $ academic_progress += 2
            $ quiz_done = True
            p "Đọc đề."
            p "Hiểu đề."
            p "Code."
            p "Debug."
            p "Không panic."
            n "PLAYER vừa vô tình thực hiện quy trình phát triển phần mềm đúng chuẩn."
            centered "Achievement unlocked: PROFESSIONAL HUMAN BEING"
        "Hoảng loạn ngay lập tức.":
            p "AAAAAAAAAAAAAAAA."
            m "Bro?"
            p "STACK OVERFLOW."
            m "Ông còn chưa mở IDE."
            p "TÔI BIẾT."
            $ sanity -= 20
            $ pending_tasks += 1

    call check_failure
    jump scene_03_break


label scene_03_break:
    scene hallway with fade
    show player at left
    show minh at right
    centered "09:30 AM — BREAK TIME"
    n "PLAYER bước ra hành lang."
    n "Energy: đang tụt nhanh."
    m "Xuống căn tin không?"
    n "PLAYER nhìn điện thoại."
    n "Có ba notification."
    play sound sfx_notification
    centered "GROUP PROJECT"
    l "@everyone có ai rảnh meeting tí không?"
    p "Không."
    play sound sfx_notification
    n "Notification thứ hai."
    l "10 phút thôi."
    p "KHÔNG."
    play sound sfx_notification
    n "Notification thứ ba."
    l "Quan trọng nha."
    with hpunch
    play sound sfx_boss
    call screen boss_title("QUICK MEETING", "Threat Level: ★★★★★")

    menu:
        "Đi ăn.":
            scene canteen with dissolve
            show player at left
            show minh at right
            p "Con người cần glucose."
            m "Chính xác."
            $ energy += 20
            $ sanity += 10
            $ escape_point += 1
        "Join meeting.":
            n "Video call opens."
            show linh at center with dissolve
            l "Ok meeting nhanh thôi nha."
            centered "09:35"
            scene hallway with fade
            show player at left
            show linh at right
            centered "10:47"
            p "..."
            l "Ok còn một vấn đề nhỏ nữa."
            p "Cái meeting này đã tồn tại lâu hơn một số nền văn minh."
            $ energy -= 25
            $ sanity -= 15
            $ academic_progress += 1
            # A meeting can clear an existing task, but the count cannot go negative.
            $ pending_tasks = max(0, pending_tasks - 1)

    call check_failure
    jump scene_04_group_project


label scene_04_group_project:
    scene classroom with dissolve
    show player at left
    show linh at center
    show minh at right
    centered "11:00 AM — GROUP PROJECT"
    l "Project hiện đang có một bug nhỏ."
    p "Bug gì?"
    l "Không chạy."
    p "Đó không phải bug nhỏ."
    m "Máy tôi chạy."
    p "Commit chưa?"
    m "Rồi."
    p "Push chưa?"
    m "..."
    p "Minh."
    m "À."
    p "MINH."
    m "Quên."
    n "PLAYER nhìn vào khoảng không."
    n "Một lập trình viên vừa trải nghiệm năm giai đoạn đau buồn."
    centered "Denial.\nAnger.\nBargaining.\nDepression.\nGit pull."

    menu:
        "Fix project ngay.":
            $ energy -= 15
            $ academic_progress += 2
            $ group_task_done = True
            $ escape_point += 1
            p "Không sao."
            p "Fix sớm thì chiều về sớm."
            n "Foreshadowing detected."
        "“Chiều làm.”":
            p "Để chiều đi."
            n "Một quyết định mà hàng triệu sinh viên trước đây cũng từng đưa ra."
            n "Không ai trong số họ vui vẻ vào buổi tối."
            $ pending_tasks += 2

    call check_failure
    jump scene_05_lunch


label scene_05_lunch:
    scene canteen with fade
    show player at left
    show minh at right
    centered "12:00 PM — LUNCH"
    n "PLAYER đứng trước đồ ăn."
    p "Cuối cùng."
    m "Ăn xong làm assignment nha."
    p "Minh."
    m "Gì?"
    p "Tại sao ông không bao giờ nói về phim ảnh?"
    m "Ờ."
    p "Âm nhạc?"
    m "Ờ."
    p "Game?"
    m "Ờ."
    p "Tình yêu?"
    m "Ờ."
    p "MỖI LẦN ÔNG MỞ MIỆNG LÀ PROJECT."
    m "Deadline mai."
    p "Understandable."

    menu:
        "Ăn đàng hoàng.":
            $ energy += 30
            $ sanity += 10
        "Vừa ăn vừa code.":
            $ academic_progress += 1
            $ energy += 10
            $ sanity -= 10
            p "Laptop."
            p "Cơm."
            p "Laptop."
            p "Cơm."
            m "Ông đang sống nguy hiểm."
            p "Tôi học công nghệ."
            p "Tôi chưa từng được sống an toàn."

    call check_failure
    jump scene_06_windows_update


label scene_06_windows_update:
    scene computer_lab with fade
    show player at left
    show minh at right
    centered "13:30 — COMPUTER LAB"
    p "Ok."
    p "Chỉ cần code nốt."
    play sound sfx_windows_error
    call screen boss_title("WINDOWS UPDATE", "Working on updates. Please don't turn off your computer.")
    centered "WINDOWS IS UPDATING — 3%%"
    p "..."
    p "Không."
    centered "4%%"
    p "Không."
    centered "5%%"
    p "TAO NÓI KHÔNG."
    with hpunch
    n "Boss thứ hai đã xuất hiện."
    m "Máy tui bình thường."
    p "Đừng nói chuyện với tôi."
    centered "15 phút sau."
    centered "7%%"
    p "Tiến bộ."
    m "2%%."
    p "TIẾN BỘ."

    menu:
        "Dùng laptop cá nhân.":
            $ energy -= 5
            $ academic_progress += 2
            $ escape_point += 1
        "Ngồi nhìn update.":
            $ sanity -= 20
            p "Có lẽ đây là lúc suy ngẫm về cuộc đời."
            n "PLAYER bắt đầu nhớ lại những lựa chọn dẫn mình đến ngành công nghệ."

    call check_failure
    jump scene_07_assignment


label scene_07_assignment:
    scene classroom_evening with fade
    show player at left
    show minh at right
    show thaydev at center
    centered "15:45 — TIẾT CUỐI"
    p "Gần rồi."
    p "Chỉ còn 75 phút."
    n "PLAYER nhìn ra cửa sổ."
    n "Ánh nắng chiều."
    n "Chim bay."
    n "Tự do."
    dev "Trước khi kết thúc..."
    stop music fadeout 0.2
    p "..."
    m "..."
    dev "Thầy có một bài assignment nhỏ."
    crowd "AAAAAAAAAAAAAAAAAAAA."
    dev "Không khó."
    p "Đừng nói câu đó."
    dev "Hạn tối nay."
    play sound sfx_notification
    with flash
    show colms at right with dissolve
    lms "23:59."
    p "AAAAAAAAAAAAA."
    # The new assignment is still pending until the bad route submits it.
    $ pending_tasks += 1
    call check_failure
    jump scene_08_final_choice


label scene_08_final_choice:
    scene classroom_evening with fade
    show player at left
    show minh at right
    centered "16:55 — FINAL FIVE MINUTES"
    n "PLAYER nhìn đồng hồ."
    n "16:55."
    n "Ba lô đã đóng."
    n "Laptop đã shutdown."
    p "Không gì có thể ngăn mình nữa."
    play sound sfx_notification
    n "Notification."
    l "@everyone."
    p "..."
    l "Có ai ở lại fix một xíu không?"
    p "Không."
    m "Ông về hả?"
    p "Đúng."
    m "Assignment thì sao?"
    p "Làm ở nhà."
    m "Project?"
    p "Git tồn tại vì một lý do."
    m "Meeting?"
    p "Discord tồn tại vì một lý do."
    m "Lab?"
    p "Remote desktop tồn tại vì một lý do."
    m "Thầy?"
    p "Thầy cũng cần về nhà."

    menu:
        "ĐI VỀ.":
            $ escape_point += 2
            $ chose_to_stay = False
            jump attempt_escape
        "“Ở lại một chút.”":
            $ chose_to_stay = True
            jump bad_ending


label attempt_escape:
    p "Không."
    p "Hôm nay kết thúc ở đây."
    n "PLAYER bước về phía thang máy."
    centered "17:00"
    n "Sau mười tiếng chiến đấu..."
    n "PLAYER cuối cùng đã nhìn thấy nó."
    n "Cánh cổng."
    n "Ánh nắng."
    n "Bầu trời."
    n "Tự do."
    scene school_gate with fade
    show player at left
    show baove at right with dissolve
    if can_escape_school():
        guard "Về hả em?"
        p "Dạ."
        guard "Ừ về đi."
        p "..."
        p "Chú."
        guard "Hử?"
        p "Cháu sẽ không bao giờ quên chú."
        guard "?"
        $ escaped_school = True
        jump good_ending
    else:
        # A weak escape attempt loops back into the screenplay's night route.
        guard "Về hả em?"
        p "Dạ."
        play sound sfx_notification
        lms "23:59."
        n "PLAYER nhìn danh sách việc còn lại. Cánh cổng bỗng xa như một deadline."
        $ chose_to_stay = False
        jump bad_ending


label check_failure:
    # Thresholds are checked after each cluster of screenplay choices.
    if energy <= 0 or pending_tasks >= 6:
        $ chose_to_stay = False
        jump bad_ending
    return
