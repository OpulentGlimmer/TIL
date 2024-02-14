```python
import webbrowser

webbrowser.open('google.com')

# ctrl + /
# webbrowser.open('https://finance.naver.com/item/main.naver?code=005930')
# webbrowser.open('https://finance.naver.com/item/main.naver?code=000660')
# webbrowser.open('https://finance.naver.com/item/main.naver?code=005380')

for code in ['005930','000660','005380']:
    webbrowser.open_new_tab(f'https://finance.naver.com/item/main.naver?code={code}')
```

### O / X
### 문법에 맞게 말 하느냐
### 컴퓨터가 알아 듣느냐

```python
print('hello')
```
### Good or Bad
### 반복적으로 코드를 쓰고 있지 않은지
### 다른 사람이 읽을 때, 쉽게 이해할 수 있는지