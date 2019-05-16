from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
# using get_text to access the inner text in the element
soup = BeautifulSoup(html, "html.parser")
# for el in soup.select(".special"):
#     print(el.get_text())

# using name to access tag name
# for el in soup.select(".special"):
#     print(el.name)

# using attrs to access to attributes
for el in soup.select(".special"):
    print(el.attrs)


