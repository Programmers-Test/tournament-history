# libot-lb
*Dự trên https://github.com/lightningbolts/Lichess-Bot-Leaderboards và https://github.com/TheYoBots/libot-lb*

Bảng xếp hạng dành cho tất cả Lichess Bot được tạo từ các video hưóng dẫn cách làm Bot từ TungJohn.

Hãy xem thử tại đây: https://thi-vua-lay-tot.github.io/libot-leaderboard/

# Tạo bảng xếp hạng
1. Đặt bí mật môi trường:

Nhận [Mã Token từ lichess (Không yêu cầu phạm vi)](https://lichess.org/account/oauth/token/create?scopes[]=None&description=Bot+Leaderboard+Token) và thực hiện lệnh sau::
```
# windows
set TOKEN='token-của-bạn'

# linux
export TOKEN='your-token-here'
```
2. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```
3. Chạy lệnh:
```bash
python bot_leaderboard.py
```

## Luật để Bot có thể vào BXH
1. Bot của bạn phải chơi ít nhất 1 trò chơi được xếp hạng trong loại Biến thể/Trò chơi tương ứng đó.
2. Bot của bạn không được có dấu vi phạm [Điều khoản dịch vụ của Lichess](https://lichess.org/terms-of-service).
