
# %%
def test_url(test_url):
    split_url = test_url.split("/")
    if len(split_url) < 5:
        return False
    if split_url[2] != "github.com":
        return False
    if split_url[0] != "https:":
        split_url[0] = "https:"
    return True
       

# %%
print(test_url("https://github.com/Author/Repo"))
print(test_url("https://github.com/Author"))
print(test_url("http://github.com"))




# %%



