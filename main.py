import glob
import frontmatter
import csv
import markdown


markdown_files = glob.glob("<path_to_md_files>/*.md")
data = []

for item in markdown_files:
    with open(item, encoding="utf-8") as f:
        print(item)
        post = frontmatter.load(f)
        
        data.append([
            post.get('title'),
            post.get('meta_title'),
            post.get('meta_description'),
            post.get('date'),
            post.get('image'),
            post.get('categories'),
            post.get('tags'),
            post.get('slug'),
            markdown.markdown(post.content)        
        ])

print(len(data))

with open('data.csv', 'w', encoding="utf-8", newline='') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerow(['title', 'meta_title', 'meta_description', 'date', 'image', 'categories', 'tags', 'slug', 'body'])
    wr.writerows(data)