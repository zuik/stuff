# Neat things about Visual Studio Code

## Search and multiple cursors

Say you have a bunch of items like this:

```
- Blah
- Clah
- Dlah
- Elah
- Flah
```
and you would like to convert all of them to proper HTML `<li>` elements. It is as easy as.

1. Find all the bullet point by searching for “- “
2. Press ESC (for some weird reason)
3. Ctrl (Command) + F2
4. Change all of those cursor to `<li>` tags

And you should be able to get the result in no time.
```html
<ul>
    <li>Blah</li>
    <li>Clah</li>
    <li>Dlah</li>
    <li>Elah</li>
    <li>Flah</li>
</ul>
```