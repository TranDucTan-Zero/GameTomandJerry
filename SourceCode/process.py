import random  # Import thư viện random để tạo các giá trị ngẫu nhiên
from sys import exit  # Import hàm exit từ thư viện sys để thoát khỏi chương trình
from var import *  # Import tất cả các biến từ một module var
from os import remove  # Import hàm remove từ thư viện os để xóa file

# Hàm tạo game với thông tin về cửa sổ và âm thanh cơ bản
def create_game(name):
    pygame.init()  # Khởi tạo pygame
    screen = pygame.display.set_mode((1366, 768))  # Tạo cửa sổ với kích thước 1366x768
    pygame.display.set_caption(name)  # Đặt tiêu đề của cửa sổ là 'name'
    pygame.display.set_icon(pygame.image.load('../Data/image/spcat.png'))  # Đặt biểu tượng cho cửa sổ
    load_music(all_music()['bg'], 0.2).play(-1)  # Phát nhạc nền với âm lượng 0.2
    return screen  # Trả về đối tượng màn hình của pygame

# Hàm ghi thông tin về trò chơi vào file
def w_file(lv_game, lv_gun, score, hp):
    s = [str(lv_game) + '\n', str(lv_gun) + '\n', str(score) + '\n', str(hp) + '\n']  # Tạo danh sách chuỗi
    with open('../Data/save/save.txt', 'w') as file:  # Mở file để ghi
        file.writelines(s)  # Ghi danh sách chuỗi vào file

# Hàm đọc thông tin về trò chơi từ file
def r_file():
    x = []  # Khởi tạo danh sách rỗng
    with open('../Data/save/save.txt') as file:  # Mở file để đọc
        for line in file:  # Lặp qua từng dòng trong file
            x.append(int(line.strip()))  # Chuyển đổi và thêm dòng vào danh sách
    return x  # Trả về danh sách chứa thông tin về trò chơi

# Hàm đóng chương trình
def close():
    pygame.quit()  # Thoát khỏi pygame
    exit()  # Thoát khỏi chương trình

# Hàm load âm nhạc với đường dẫn và âm lượng cho trước
def load_music(path, vol):
    sound = pygame.mixer.Sound(path)  # Tạo đối tượng âm thanh từ đường dẫn
    sound.set_volume(vol)  # Đặt âm lượng cho âm thanh
    return sound  # Trả về đối tượng âm thanh

# Hàm kiểm tra va chạm giữa hai đối tượng
def collision(inf_1, inf_2):
    for i in range(len(inf_1['pos'])):  # Lặp qua tất cả các vị trí của đối tượng 1
        inf_1['rect'].topleft = inf_1['pos'][i]  # Đặt vị trí cho đối tượng 1
        for j in range(len(inf_2['pos'])):  # Lặp qua tất cả các vị trí của đối tượng 2
            inf_2['rect'].topleft = inf_2['pos'][j]  # Đặt vị trí cho đối tượng 2
            if (inf_1['rect']).colliderect(inf_2['rect']):  # Kiểm tra va chạm giữa hai hình chữ nhật
                return [i, j]  # Trả về chỉ số của hai đối tượng
    return None  # Trả về None nếu không có va chạm nào

# Hàm thay đổi vị trí theo hai tuple
def change_pos(tuple_1, tuple_2):
    return tuple(a + b for a, b in zip(tuple_1, tuple_2))  # Tính tổng các phần tử tương ứng từ hai tuple

# Hàm thêm sự kiện và thiết lập thời gian cho sự kiện
def add_event(id_event, timer):
    x = pygame.USEREVENT + id_event  # Tạo một loại sự kiện mới
    pygame.time.set_timer(x, timer)  # Đặt thời gian cho sự kiện
    return x  # Trả về loại sự kiện mới

# Hàm hiển thị điểm và máu trên màn hình
def show_score_hp(screen, score, hp):
    temp = text(f"x{score}", 50, 'Yellow')  # Tạo đối tượng văn bản cho điểm
    screen.blit(temp, (50, 0))  # Vẽ điểm lên màn hình
    temp = text(f"x{hp}", 50, 'Brown')  # Tạo đối tượng văn bản cho máu
    screen.blit(temp, (50, 60))  # Vẽ máu lên màn hình

# Hàm hiển thị màn hình chơi
def screen_playing(screen, obj, pl_inf, ck_inf, egg_inf, ls_inf, score_inf, score, hp, time):
    for i, j in obj:  # Lặp qua tất cả các đối tượng trong obj
        screen.blit(i, j)  # Vẽ đối tượng lên màn hình
    for i in ls_inf['pos']:  # Lặp qua tất cả các vị trí của laser
        screen.blit(ls_inf['img'], i)  # Vẽ laser lên màn hình
    for i in ck_inf['pos']:  # Lặp qua tất cả các vị trí của chicken
        screen.blit(ck_inf['img'], i)  # Vẽ chicken lên màn hình
    for i in egg_inf['pos']:  # Lặp qua tất cả các vị trí của egg
        screen.blit(egg_inf['img'], i)  # Vẽ egg lên màn hình
    for i in score_inf['pos']:  # Lặp qua tất cả các vị trí của score
        screen.blit(score_inf['img'], i)  # Vẽ score lên màn hình
    show_score_hp(screen, score, hp)  # Hiển thị điểm và máu
    screen.blit(text(f"Time remaining: {time}", 30, 'Red'), (1100, 700))  # Hiển thị thời gian còn lại
    screen.blit(pl_inf['img'], pl_inf['pos'][0])  # Vẽ player lên màn hình
    pygame.display.update()  # Cập nhật màn hình

# Hàm thêm vị trí cho menu
def add_pos_menu(obj_menu):
    new_arr = [[obj_menu[0], (500, 100)]]  # Tạo một danh sách mới với phần tử đầu tiên
    pos_y = 350  # Đặt giá trị y ban đầu
    for i in range(1, len(obj_menu)):  # Lặp qua từng phần tử trong obj_menu, bắt đầu từ phần tử thứ hai
        new_arr.append([obj_menu[i], (600, pos_y)])  # Thêm phần tử mới vào danh sách
        pos_y += 100  # Tăng giá trị y
    return new_arr  # Trả về danh sách mới

# Hàm tạo menu với các tùy chọn và đặt vị trí cho các tùy chọn
def create_menu(screen, menu):
    obj = add_pos_menu(menu)  # Tạo menu với các tùy chọn và đặt vị trí
    bg = get_img('bg')  # Lấy hình nền từ hàm get_img
    signal = text('>>>', 50, 'White')  # Tạo dấu hiệu chọn
    pos_sgn = (obj[1][1][0] - 80, obj[1][1][1])  # Đặt vị trí cho dấu hiệu chọn
    fps = pygame.time.Clock()  # Tạo đối tượng Clock cho pygame
    select = 1  # Đặt lựa chọn ban đầu là 1
    while True:  # Lặp vô hạn
        fps.tick(15)  # Giữ tốc độ cập nhật ở mức 15 FPS
        screen.blit(bg, (0, 0))  # Vẽ hình nền lên màn hình
        screen.blit(signal, pos_sgn)  # Vẽ dấu hiệu chọn lên màn hình
        for i, j in obj:  # Lặp qua tất cả các tùy chọn trong obj
            screen.blit(i, j)  # Vẽ tùy chọn lên màn hình
        pygame.display.update()  # Cập nhật màn hình

        for event in pygame.event.get():  # Lặp qua tất cả các sự kiện pygame
            if event.type == pygame.QUIT:  # Kiểm tra nếu sự kiện là ngắt
                close()  # Thoát khỏi chương trình
        key = pygame.key.get_pressed()  # Kiểm tra xem phím nào đã được nhấn
        if key[pygame.K_DOWN] and select < len(menu) - 1:  # Nếu phím mũi tên xuống được nhấn và lựa chọn nhỏ hơn số tùy chọn
            select += 1  # Tăng lựa chọn lên 1
            pos_sgn = change_pos(pos_sgn, (0, 100))  # Di chuyển dấu hiệu chọn xuống dưới
        elif key[pygame.K_UP] and select > 1:  # Nếu phím mũi tên lên được nhấn và lựa chọn lớn hơn 1
            select -= 1  # Giảm lựa chọn đi 1
            pos_sgn = change_pos(pos_sgn, (0, -100))  # Di chuyển dấu hiệu chọn lên trên
        elif key[pygame.K_RETURN]:  # Nếu phím Enter được nhấn
            return select  # Trả về lựa chọn hiện tại

# Hàm tạo jerry với số lượng và vị trí cụ thể
def create_jerry(level, number_jr, jr_inf):
    distance = 80  # Đặt khoảng cách giữa các jerry
    x = 100  # Đặt vị trí x ban đầu
    y = 0  # Đặt vị trí y ban đầu
    direct = False  # Đặt hướng ban đầu của jerry
    if level < 4:  # Nếu cấp độ nhỏ hơn 4
        jr_inf['pos'].append((x, y))  # Thêm vị trí đầu tiên cho jerry
        for i in range(1, number_jr):  # Lặp qua từng jerry còn lại
            if i % 15 == 0:  # Nếu đến hàng tiếp theo
                x = 100  # Đặt lại vị trí x
                y += 100  # Tăng vị trí y
            else:
                x += distance  # Tăng vị trí x
            jr_inf['pos'].append((x, y))  # Thêm vị trí mới cho jerry
        return  # Kết thúc hàm nếu cấp độ nhỏ hơn 4
    else:
        jr_row = 10  # Đặt số lượng jerry trên mỗi hàng ban đầu
        if level == 5:  # Nếu cấp độ là 5
            jr_row = 15  # Tăng số lượng jerry trên mỗi hàng lên 15
        jr_inf['pos'].append((x, y))  # Thêm vị trí đầu tiên cho jerry
        jr_inf['direct'].append(direct)  # Thêm hướng ban đầu của jerry
        for i in range(1, number_jr):  # Lặp qua từng jerry còn lại
            if i % jr_row == 0:  # Nếu đến hàng tiếp theo
                if direct:  # Nếu hướng hiện tại là True
                    x = 100  # Đặt lại vị trí x
                    direct = False  # Đổi hướng
                else:
                    x = 500  # Đặt lại vị trí x
                    direct = True  # Đổi hướng
                y += 100  # Tăng vị trí y
            else:
                x += distance  # Tăng vị trí x
            jr_inf['pos'].append((x, y))  # Thêm vị trí mới cho jerry
            jr_inf['direct'].append(direct)  # Thêm hướng mới của jerry

# Hàm tạo laser với số lượng và vị trí cụ thể
def create_laser(num_ray, ls_inf, pl_inf, sound):
    if num_ray == 1:  # Nếu số lượng laser là 1
        ls_inf['pos'].append(change_pos(pl_inf['pos'][0], (20, -20)))  # Thêm vị trí cho laser
        sound.play()  # Phát âm thanh
    elif num_ray == 2:  # Nếu số lượng laser là 2
        ls_inf['pos'].append(change_pos(pl_inf['pos'][0], (0, -20)))  # Thêm vị trí cho laser thứ nhất
        ls_inf['pos'].append(change_pos(pl_inf['pos'][0], (40, -20)))  # Thêm vị trí cho laser thứ hai
        sound.play()  # Phát âm thanh
    elif num_ray == 3:  # Nếu số lượng laser là 3
        ls_inf['pos'].append(change_pos(pl_inf['pos'][0], (-20, -20)))  # Thêm vị trí cho laser thứ nhất
        ls_inf['pos'].append(change_pos(pl_inf['pos'][0], (60, -20)))  # Thêm vị trí cho laser thứ hai
        ls_inf['pos'].append(change_pos(pl_inf['pos'][0], (20, -20)))  # Thêm vị trí cho laser thứ ba
        sound.play()  # Phát âm thanh

# Hàm tạo xfish với cấp độ và vị trí cụ thể
def create_xfish(level, xf_inf, jr_inf):
    if len(jr_inf['pos']) and level < 4:  # Nếu còn jerry và cấp độ nhỏ hơn 4
        temp = random.randint(0, len(jr_inf['pos']) - 1)  # Chọn một vị trí ngẫu nhiên từ jerry
        xf_inf['pos'].append(change_pos(jr_inf['pos'][temp], (10, 50)))  # Thêm vị trí mới cho xfish
    elif len(jr_inf['pos']) and level >= 4:  # Nếu còn jerry và cấp độ lớn hơn hoặc bằng 4
        temp = random.randint(0, len(jr_inf['pos']) - 1)  # Chọn một vị trí ngẫu nhiên từ jerry
        xf_inf['pos'].append(change_pos(jr_inf['pos'][temp], (10, 50)))  # Thêm vị trí mới cho xfish
        xf_inf['direct'].append(jr_inf['direct'][temp])  # Thêm hướng mới cho xfish

# Hàm di chuyển tất cả các đối tượng trong danh sách
def move(speed, inf):
    for i in range(len(inf['pos'])):  # Lặp qua tất cả các vị trí trong danh sách
        inf['pos'][i] = change_pos(inf['pos'][i], (0, speed))  # Di chuyển mỗi vị trí theo chiều y

# Hàm di chuyển jerry
def move_jr(inf):
    get_dir = {  # Tạo một từ điển đối với các hướng di chuyển của jerry
        True: -1,  # Hướng True di chuyển qua trái
        False: 1  # Hướng False di chuyển qua phải
    }
    for i in range(len(inf['pos'])):  # Lặp qua tất cả các vị trí trong danh sách
        inf['pos'][i] = change_pos(inf['pos'][i], (get_dir[inf['direct'][i]], 0))  # Di chuyển mỗi vị trí theo hướng tương ứng

# Hàm di chuyển xfish
def move_xfs(inf):
    get_dir = {  # Tạo một từ điển đối với các hướng di chuyển của xfish
        True: -1,  # Hướng True di chuyển qua trái
        False: 1  # Hướng False di chuyển qua phải
    }
    for i in range(len(inf['pos'])):  # Lặp qua tất cả các vị trí trong danh sách
        inf['pos'][i] = change_pos(inf['pos'][i], (get_dir[inf['direct'][i]], 2))  # Di chuyển mỗi vị trí theo hướng tương ứng

# Hàm kiểm tra các đối tượng ra khỏi màn hình và xóa chúng khỏi danh sách
def out_screen(inf, size_screen):
    for i in inf['pos']:  # Lặp qua tất cả các vị trí trong danh sách
        if i[0] > size_screen[0] or i[0] < 0 or i[1] > size_screen[1] or i[1] < 0:  # Kiểm tra xem vị trí có nằm ngoài màn hình không
            inf['pos'].remove(i)  # Nếu có, xóa vị trí đó khỏi danh sách

# Hàm kiểm tra các xfish ra khỏi màn hình và xóa chúng khỏi danh sách
def out_screen_xf(level, inf, size_screen):
    for i in inf['pos']:  # Lặp qua tất cả các vị trí trong danh sách
        if i[0] > size_screen[0] or i[0] < 0 or i[1] > size_screen[1] or i[1] < 0:  # Kiểm tra xem vị trí có nằm ngoài màn hình không
            if level > 3:  # Nếu cấp độ lớn hơn 3
                del inf['direct'][inf['pos'].index(i)]  # Xóa hướng tương ứng với vị trí
            inf['pos'].remove(i)  # Xóa vị trí đó khỏi danh sách

# Hàm hiển thị thông điệp trên màn hình
def screen_show_mess(screen, string):
    screen.blit(get_img('bg'), (0, 0))  # Vẽ hình nền lên màn hình
    screen.blit(text(string, 100, 'Red'), (500, 200))  # Vẽ thông điệp lên màn hình với màu đỏ và kích thước 100
    pygame.display.update()  # Cập nhật màn hình

# Hàm lặp chơi trò chơi
def loop_playing(screen, load=None):
    if load is None:  # Nếu không có dữ liệu load
        load = [1, 1, 0, 5]  # Đặt dữ liệu mặc định
    lv_game, lv_gun, score, hp = load[0], load[1], load[2], load[3]  # Gán các giá trị từ dữ liệu load
    if lv_game > 1:  # Nếu cấp độ lớn hơn 1
        w_file(lv_game, lv_gun, score, hp)  # Ghi dữ liệu vào file

    shoot_time = 0  # Đặt thời gian bắn laser
    num_jr = 1  # Số lượng jerry ban đầu
    num_create_jr = 2  # Số lần tạo jerry
    max_time = 3  # Thời gian tối đa
    req_plus_hp = 4  # Yêu cầu tăng máu
    min_req_score = 5  # Yêu cầu điểm tối thiểu
    game = game_level()  # Lấy dữ liệu về cấp độ trò chơi

    ray_gun = 1  # Số lượng laser mỗi lần bắn
    speed_gun = 2  # Tốc độ di chuyển của laser
    req_score_gun = 3  # Yêu cầu điểm để nâng cấp súng
    gun = gun_level()  # Lấy dữ liệu về cấp độ súng

    screen_show_mess(screen, f"LEVEL {lv_game}")  # Hiển thị thông điệp về cấp độ trò chơi
    pygame.time.delay(3000)  # Delay 3 giây

    fps = pygame.time.Clock()  # Tạo đối tượng Clock cho pygame
    Max = pygame.display.get_window_size()  # Lấy kích thước của cửa sổ hiện tại
    music = all_music()  # Lấy dữ liệu về âm nhạc

    pl_inf = playertom_inf()  # Lấy thông tin về player
    jr_inf = jerry_inf()  # Lấy thông tin về jerry
    ls_inf = laser_inf()  # Lấy thông tin về laser
    xf_inf = xfish_inf()  # Lấy thông tin về xfish
    score_inf = sc_inf()  # Lấy thông tin về điểm

    size_player = pl_inf['img'].get_size()  # Lấy kích thước của player
    laser_sound = load_music(music['shoot'], 0.05)  # Tải âm thanh bắn laser
    boom_sound = load_music(music['explode_ck'], 0.05)  # Tải âm thanh nổ của jerry
    collision_sound = load_music(music['collision'], 0.05)  # Tải âm thanh va chạm

    create_jerry(lv_game, game[lv_game][num_jr], jr_inf)  # Tạo jerry ban đầu

    game[lv_game][num_create_jr] -= 1  # Giảm số lần tạo jerry

    ls_speed = add_event(0, gun[lv_gun][shoot_time])  # Tạo sự kiện bắn laser
    xfish_speed = add_event(1, game[lv_game][shoot_time])  # Tạo sự kiện tạo xfish
    countdown = add_event(2, 1000)  # Tạo sự kiện đếm ngược

    count = game[lv_game][max_time]  # Đặt thời gian đếm ngược

    obj = obj_default_playing()  # Lấy đối tượng mặc định

    plus_hp = False  # Biến kiểm tra tăng máu

    while True:  # Vòng lặp chính của trò chơi
        fps.tick(60)  # Đặt FPS cho trò chơi

        screen_playing(screen, obj, pl_inf, jr_inf, xf_inf, ls_inf, score_inf, score, hp, count)  # Hiển thị màn hình chơi

        # Xử lý sự kiện
        for event in pygame.event.get():
            # Đóng ứng dụng
            if event.type == pygame.QUIT:
                close()
            # Tạo laser
            elif event.type == ls_speed:
                create_laser(gun[lv_gun][ray_gun], ls_inf, pl_inf, laser_sound)
            # Tạo xfish
            elif event.type == xfish_speed:
                create_xfish(lv_game, xf_inf, jr_inf)
            # Đếm ngược
            elif event.type == countdown:
                count -= 1

        # Tạo jerry mới nếu cần
        if game[lv_game][num_create_jr] > 0 and (len(jr_inf['pos']) == 0 and len(score_inf['pos']) == 0):
            create_jerry(lv_game, game[lv_game][num_jr], jr_inf)
            game[lv_game][num_create_jr] -= 1

        # Tăng máu nếu cần
        if score % game[lv_game][req_plus_hp] == 0 and score != 0 and plus_hp is False:
            hp += 1
            plus_hp = True

        # Kiểm tra kết thúc cấp độ hoặc trò chơi
        if (len(jr_inf['pos']) == 0 and len(score_inf['pos']) == 0) or (
                count == 0 and score >= game[lv_game][min_req_score]):
            lv_game += 1
            w_file(lv_game, lv_gun, score, hp)
            load = [lv_game, lv_gun, score, hp]
            break
        elif count == 0 or hp == 0:
            screen_show_mess(screen, 'Tom đã thua')
            pygame.time.delay(3000)
            if lv_game != 1:
                remove('../Data/save/save.txt')
            return

        # Nâng cấp súng
        if score >= gun[lv_gun][req_score_gun] and lv_gun < len(gun):
            lv_gun += 1
            pygame.time.set_timer(ls_speed, gun[lv_gun][shoot_time])

        # Xóa đối tượng ra khỏi màn hình
        out_screen(ls_inf, Max)
        out_screen(score_inf, Max)
        out_screen_xf(lv_game, xf_inf, Max)

        # Di chuyển đối tượng
        if lv_game > 3:
            move_jr(jr_inf)
            move_xfs(xf_inf)
        else:
            move(2, xf_inf)
        move(- gun[lv_gun][speed_gun], ls_inf)
        move(1, score_inf)

        # Xóa jerry khi bị bắn
        check = collision(ls_inf, jr_inf)
        if check is not None:
            boom_sound.play()
            screen.blit(jr_inf['img_explode'], jr_inf['pos'][check[1]])
            pygame.display.update()
            score_inf['pos'].append(jr_inf['pos'][check[1]])
            ls_inf['pos'].pop(check[0])
            jr_inf['pos'].pop(check[1])
            if lv_game > 3:
                jr_inf['direct'].pop(check[1])

        # Xóa xfish khi va chạm
        check = collision(xf_inf, pl_inf)
        if check is not None:
            collision_sound.play()
            screen.blit(pl_inf['img_explode'], pl_inf['pos'][check[1]])
            pygame.display.update()
            pygame.time.delay(20)
            xf_inf['pos'].pop(check[0])
            if lv_game > 3:
                xf_inf['direct'].pop(check[0])
            hp -= 1

        # Tăng điểm khi ăn điểm
        check = collision(score_inf, pl_inf)
        if check is not None:
            score_inf['pos'].pop(check[0])
            score += 1
            plus_hp = False

        # Di chuyển người chơi
        key = pygame.key.get_pressed()
        pos_x, pos_y = pl_inf['pos'][0]
        more_max_w = pos_x - pl_inf['move'] > 0
        less_max_w = pos_x + pl_inf['move'] + size_player[0] <= Max[0]
        more_half_h = pos_y - pl_inf['move'] > Max[1] // 2
        less_max_h = pos_y + pl_inf['move'] + size_player[1] <= Max[1]
        if (key[pygame.K_LEFT] or key[pygame.K_a]) and more_max_w:
            pl_inf['pos'][0] = change_pos(pl_inf['pos'][0], (-pl_inf['move'], 0))
        elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and less_max_w:
            pl_inf['pos'][0] = change_pos(pl_inf['pos'][0], (pl_inf['move'], 0))
        elif (key[pygame.K_UP] or key[pygame.K_w]) and more_half_h:
            pl_inf['pos'][0] = change_pos(pl_inf['pos'][0], (0, -pl_inf['move']))
        elif (key[pygame.K_DOWN] or key[pygame.K_s]) and less_max_h:
            pl_inf['pos'][0] = change_pos(pl_inf['pos'][0], (0, pl_inf['move']))
        elif key[pygame.K_ESCAPE]:
            choose = create_menu(screen, menu_pause())
            if choose == 2:
                break
    if load[0] < len(game):
        loop_playing(screen, load)
    else:
        screen_show_mess(screen, 'Tom đã chiến thắng')
    return
