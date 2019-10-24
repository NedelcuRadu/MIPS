```python
text = "Apanapa apa aparepe meperepe."
text = text.split()
siruri = ["pa", "pe", "pi", "po", "pu"]
for cuv in text:
    for sir in siruri:
        while sir in cuv:
            cuv = cuv.replace(sir, "")
    print(cuv, end=" ")

```
