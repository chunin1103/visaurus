def generate_sitemap(popular_words, output_file):
    with open(output_file, "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

        # Home page
        f.write('  <url>\n')
        f.write('    <loc>http://tudiendongnghia.com/</loc>\n')
        f.write('    <changefreq>weekly</changefreq>\n')
        f.write('  </url>\n')

        # Search result pages
        for word in popular_words:
            slug = word.replace(" ", "-")
            f.write('  <url>\n')
            f.write(f'    <loc>http://tudiendongnghia.com/search/{slug}</loc>\n')
            f.write('    <changefreq>monthly</changefreq>\n')
            f.write('  </url>\n')

        f.write('</urlset>\n')

if __name__ == "__main__":
    with open("popular_words.txt", "r") as f:
        popular_words
