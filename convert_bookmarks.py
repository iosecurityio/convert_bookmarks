import json


def convert_bookmarks_to_html(bookmarks_file, output_file):
    """Converts the Bookmarks file that is saved as a JSON config file on the hard drive 
    to an HTML file "Export".

    This effectively does the same thing as when you export your bookmarks from Chrome, 
    so that they can be imported into another browser later."""

    with open(bookmarks_file, 'r') as f:
        data = json.load(f)

    bookmarks = data['roots']['bookmark_bar']['children']

    # The ChatGPT Special header writer ;)
    with open(output_file, 'w') as f:
        f.write('<!DOCTYPE NETSCAPE-Bookmark-file-1>\n')
        f.write('<!-- This is an automatically generated file.\n')
        f.write('     It will be read and overwritten.\n')
        f.write('     DO NOT EDIT! -->\n')
        f.write('<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n')
        f.write('<TITLE>Bookmarks</TITLE>\n')
        f.write('<H1>Bookmarks</H1>\n')
        f.write('<DL><p>\n')

        write_bookmarks(bookmarks, f)

        f.write('</DL><p>\n')


def write_bookmarks(bookmarks, file):
    for bookmark in bookmarks:
        if 'children' in bookmark:
            file.write('<DT><H3>' + bookmark['name'] + '</H3>\n')
            file.write('<DL><p>\n')
            write_bookmarks(bookmark['children'], file)
            file.write('</DL><p>\n')
        else:
            file.write('<DT><A HREF="' +
                       bookmark['url'] + '">' + bookmark['name'] + '</A>\n')


# Example usage
convert_bookmarks_to_html('Bookmarks.json', 'Bookmarks.html')
