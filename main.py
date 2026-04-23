from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import os
import time
import random
from dotenv import load_dotenv
import sys
import io
sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer,
    encoding='utf-8',
    line_buffering=True,
    write_through=True,
)
# Hàm nộp bài
def submit_assignment(page, content, file_path):
    try:
        print(f"[*] Đang nộp bài: {content}...")

        # Chọn phần tử input để tải file
        file_input = page.locator("input[type='file']")
        file_input.set_input_files(file_path)
        time.sleep(2)

        # Nhấn nút nộp bài
        submit_button = page.locator(".submit__pad__btn")
        submit_button.click()
        print(f"[+] Đã nộp bài: {content}")
        time.sleep(2)
    except Exception as e:
        print("[-] Không tìm thấy bài giải trong folder")

# Khởi chạy bot
def startBot(username, password, login_url, list_url, folder_path, total_pages):
    with sync_playwright() as p:
        # Cấu hình trình duyệt
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        try:
            # Đăng nhập
            print("[*] Đang đăng nhập...")
            page.goto(login_url)
            time.sleep(2)
            
            page.fill("input[name='username']", username)
            page.fill("input[name='password']", password)
            page.press("input[name='password']", "Enter")
            time.sleep(3)

            # Kiểm tra đăng nhập thành công
            if "login" in page.url:
                print("[-] Đăng nhập thất bại. Kiểm tra lại username và password.")
                return
            print("[+] Đăng nhập thành công!")

            # Duyệt danh sách bài tập
            print("[*] Đang thu thập danh sách bài tập...")
            for page_number in range(1, total_pages + 1):
                url = f"{list_url}?page={page_number}"
                page.goto(url)
                time.sleep(2)

                # Lấy mã HTML của toàn bộ trang
                html_content = page.content()  # Lấy HTML của trang
                soup = BeautifulSoup(html_content, "html.parser")
                
                rows = soup.select("table tbody tr")

                print(f"\nTrang {page_number}:")
                row_index = 15
                while row_index < len(rows):
                    row = rows[row_index]
                    columns = row.find_all("td")
                    if len(columns) >= 4:
                        content = columns[2].get_text().strip()  # Lấy mã bài tập
                        title = columns[3].get_text().strip()
                        class_name = row.get("class", [])

                        # Kiểm tra trạng thái bài
                        if "bg--10th" in class_name:
                            print(f"Đã làm: {content}")
                        else:
                            print(f"Chưa làm: {content}")

                            # Truy cập bài tập và nộp bài
                            page.goto(f"{list_url}/{content}")
                            time.sleep(2)

                            check = random.randint(1, 6)
                            print(check)
                            so = random.randint(700, 900)
                            wait_seconds = 0

                            if check % 3 != 0:
                                file_path = f"{fake_path}/{content} - {title}.py"  # Thay đổi nếu là ngôn ngữ khác
                                submit_assignment(page, content, file_path)
                                #row_index -= 1
                                wait_seconds = max(0, so - 700)
                            else:
                                file_path = f"{folder_path}/{content} - {title}.py"  # Thay đổi nếu là ngôn ngữ khác
                                submit_assignment(page, content, file_path)
                                wait_seconds = max(0, so - 845)
                            print(f"[+] Đã hoàn tất lượt nộp bài cho mã: {content}")
                            print(f"[*] Đang chờ {wait_seconds} giây trước khi tiếp tục...")
                            time.sleep(wait_seconds)
                    row_index += 1 

        except Exception as e:
            print("[*] Đã xảy ra lỗi: ", e)
        finally:
            print("[*] Đã đóng trình duyệt.")
            try:
                if browser.is_connected():
                    browser.close()
            except Exception as close_error:
                print(f"[!] Bỏ qua lỗi khi đóng trình duyệt: {close_error}")

# Thông tin đăng nhập và URL
load_dotenv()
username = os.getenv("APP_USERNAME")
password = os.getenv("APP_PASSWORD")
login_url = os.getenv("LOGIN_URL")
list_url = os.getenv("LIST_URL")
folder_path = os.getenv("FOLDER_PATH")
fake_path = os.getenv("FAKE_PATH")
total_pages = int(os.getenv("TOTAL_PAGES"))

# Khởi chạy bot
startBot(username, password, login_url, list_url, folder_path, total_pages)
