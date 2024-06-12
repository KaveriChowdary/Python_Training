text=input()
left = 0
right = len(text) - 1
reversed_text = list(text)
while left <= right:
    if not text[left].isalnum():
      left += 1
    elif not text[right].isalnum():
      right -= 1
    else:
      reversed_text[left], reversed_text[right] = reversed_text[right], reversed_text[left]
      left += 1
      right -= 1
return ''.join(reversed_text)
reversed_text = reverse_with_special_chars(text)
print(reversed_text)