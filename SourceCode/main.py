from process import r_file, loop_playing, create_game, create_menu, close  # Import các hàm cần thiết từ module process
from var import menu_start, menu_load  # Import các lựa chọn menu từ module var
import os  # Import module os để thực hiện các thao tác với tệp


def main():
    # Tạo màn hình trò chơi với tiêu đề 'Tom & Jerry'
    screen = create_game('Tom & Jerry')
    # Tạo menu với các lựa chọn để bắt đầu trò chơi
    select_start = create_menu(screen, menu_start())
    # Vòng lặp vô hạn để giữ trò chơi chạy cho đến khi người chơi thoát
    while True:
        # Nếu người chơi chọn bắt đầu một trò chơi mới
        if select_start == 1:
            # Kiểm tra xem tệp lưu trò chơi có tồn tại không
            if os.path.exists('../Data/save/save.txt'):
                # Nếu tệp lưu tồn tại, yêu cầu người chơi tải hoặc bắt đầu một trò chơi mới
                select_load = create_menu(screen, menu_load())
                # Nếu người chơi chọn tải trò chơi đã lưu
                if select_load == 1:
                    # Đọc thông tin từ tệp lưu
                    load_inf = r_file()
                    # Bắt đầu vòng lặp trò chơi với thông tin đã tải
                    loop_playing(screen, load_inf)
                # Nếu người chơi chọn bắt đầu một trò chơi mới thay vì tải
                elif select_load == 2:
                    # Xóa tệp lưu hiện có
                    os.remove('../Data/save/save.txt')
                    # Bắt đầu vòng lặp trò chơi với không có thông tin đã tải (trò chơi mới)
                    loop_playing(screen)
            else:
                # Nếu không có tệp lưu tồn tại, bắt đầu một trò chơi mới
                loop_playing(screen)
            # Sau khi kết thúc trò chơi hoặc quay lại menu, yêu cầu người chơi bắt đầu trò chơi mới hoặc thoát
            select_start = create_menu(screen, menu_start())
        # Nếu người chơi chọn thoát trò chơi từ menu chính
        elif select_start == 2:
            # Đóng trò chơi
            close()


if __name__ == "__main__":
    main()
