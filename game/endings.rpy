# Both routes set persistent gallery flags at their title cards.

label good_ending:
    hide screen stats_hud
    scene bedroom_gaming with fade
    show player happy at center with dissolve
    centered "HOME — 18:02"
    n "PLAYER mở cửa phòng."
    n "Quăng balo xuống."
    n "Bật PC."
    centered "RGB LIGHTING ON."
    n "Steam startup sound."
    p "Cuối cùng..."
    n "PLAYER mở game."
    friend "Ê vô game không?"
    p "VÔ."
    friend "Mai deadline đúng không?"
    p "..."
    p "Đó là vấn đề của Future Me."
    n "Và thế là..."
    n "PLAYER đã thành công thoát khỏi trường."
    n "Không phải nhờ sức mạnh."
    n "Không phải nhờ trí thông minh."
    n "Mà nhờ kỹ năng quan trọng nhất của sinh viên năm cuối:"
    centered "BIẾT KHI NÀO NÊN ĐI VỀ."
    n "PLAYER ngồi trước PC."
    n "Một tay cầm nước."
    n "Một tay cầm chuột."
    n "Game đang loading."
    n "Điện thoại phía sau hiện: 12 unread messages — GROUP PROJECT."
    n "PLAYER úp điện thoại xuống."
    p "Không thấy."
    p "Không tồn tại."
    play sound sfx_success
    $ persistent.good_ending_unlocked = True
    $ renpy.save_persistent()
    call screen ending_card("GOOD ENDING", "ESCAPE SUCCESSFUL", "Student Status: ALIVE\nEnergy: ENOUGH FOR ONE MORE GAME\nMental Stability: QUESTIONABLE\nTomorrow: PROBLEM FOR TOMORROW\n\nAchievement unlocked: TOUCH GRASS... TOMORROW")
    call screen post_ending_actions
    return


label bad_ending:
    # Staying by choice and failing an escape both converge on the night route.
    if chose_to_stay:
        p "Thôi để tôi fix cho xong."
        m "Nice."
        l "Nice."
        lms "Nice."
        n "Narrator did not like that."
    else:
        n "Deadline giữ PLAYER lại trường lâu hơn dự tính."

    scene classroom_evening with fade
    show player exhausted at left
    show linh at center
    show minh at right
    centered "17:15"
    p "Fix xong rồi."
    $ group_task_done = True
    l "Nhân tiện..."
    centered "18:30"
    p "Xong."
    m "Assignment?"
    p "Ờ ha."
    centered "20:10"
    p "Upload."
    play sound sfx_windows_error
    lms "File format invalid."
    p "..."
    centered "21:05"
    p "UPLOAD."
    lms "Submission saved."
    $ assignment_uploaded = True
    $ pending_tasks = max(0, pending_tasks - 1)
    p "Cuối cùng."
    l "Bro."
    p "Đừng."
    l "Slide."
    p "..."
    centered "22:17"
    $ energy = min(energy, 12)
    $ sanity = min(sanity, 4)
    n "Energy: 12. Sanity: 4."
    p "Font nào?"
    m "Poppins."
    p "Ok."
    l "Hay Montserrat?"
    p "Không."
    l "Inter?"
    p "LINH."

    scene classroom_evening with fade
    show player exhausted at center
    centered "23:47"
    n "PLAYER ngồi một mình trong lớp."
    n "Màn hình laptop chiếu ánh sáng lên khuôn mặt."
    p "Done..."
    n "PLAYER đứng dậy."
    centered "CRACK."
    with hpunch
    p "?"
    n "Một cánh tay rơi xuống."
    p "..."
    p "Understandable."
    n "Sau 16 tiếng tại trường..."
    n "Cơ thể PLAYER đã hoàn tất quá trình chuyển hóa."
    n "Từ: Sinh viên."
    n "Thành: Calcium-based lifeform."
    # MainExhaust represents the screenplay's skeleton gag in this route.
    show player exhausted at center with dissolve
    n "PLAYER giờ là một bộ xương."
    n "Bộ xương đeo balo."
    n "Bộ xương cầm laptop."
    n "Bộ xương bước về phía cổng."

    scene hallway_night with fade
    show player exhausted at center
    pause 0.5
    scene campus_night with fade
    pause 0.5
    scene school_night with fade
    show player exhausted at left
    show baove at right
    centered "23:59"
    guard "Em."
    p "Dạ?"
    guard "Muộn rồi đó."
    p "Dạ em về."
    n "CHÚ BẢO VỆ nhìn PLAYER."
    guard "Em học từ sáng tới giờ à?"
    p "Dạ."
    guard "..."
    guard "Cố gắng dữ."
    p "Dạ."
    n "Một cơn gió thổi qua."
    n "Một vài cái xương bay mất."
    p "Chú đợi cháu nhặt cái xương chậu."

    $ energy = 0
    hide screen stats_hud
    scene black with fade
    play sound sfx_bad
    $ persistent.bad_ending_unlocked = True
    $ renpy.save_persistent()
    call screen ending_card("BAD ENDING", "FPT HAS CONSUMED YOU", "Student Status: DECEASED*\n*Vẫn phải đi học ngày mai.\nEnergy: 0\nSanity: SEGMENTATION FAULT\nBone Integrity: 73%\nAssignment: SUBMITTED\nGroup Project: SOMEHOW STILL NOT FINISHED")
    play sound sfx_notification
    l "@everyone sáng mai meeting 7:00 nha."
    p "..."
    p "AAAAAAAAAAAAAAAAAAAA—"
    centered "ROLL CREDITS."
    scene bedroom_morning with fade
    show player exhausted at center
    centered "06:30 AM"
    play sound sfx_alarm
    centered "RRRRRRRRRRRRRR!!!!"
    n "Skeleton hand reaches from blanket."
    p "Thêm năm phút..."
    centered "NEW GAME+\nDifficulty unlocked: SENIOR YEAR"
    call screen post_ending_actions
    return


label new_game_plus:
    $ new_game_plus = True
    jump start
