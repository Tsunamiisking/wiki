from django.shortcuts import render
from django.utils.safestring import mark_safe
import markdown
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
import random
from django.shortcuts import redirect

# def index(request):
#     if request.method == 'POST':
#         entry_name = request.POST.get('q')
        
#         if entry_name:
#             entry_content = util.get_entry(entry_name)
#             html_content = markdown.markdown(entry_content)
#             return render(request, "encyclopedia/entrypage.html", {
#                 "entryPageContent": mark_safe(html_content)
#             })
#         else:
#             return render(request, "encyclopedia/error.html")

#     return render(request, "encyclopedia/index.html", {
#         "entries": util.list_entries()
#     })

def index(request):
    if request.method == "POST":
        # If the request method is POST, handle form submission
        query = request.POST.get('q')
        if not query:
            return render(request, "encyclopedia/error.html", {
                "message" : "Page does not exist"
            })

        list_of_entries = util.list_entries()
        if query in list_of_entries:
            # Retrieve entries containing the query string
            entries = util.get_entry(query)
            html_content = markdown.markdown(entries)
            return render(request, "encyclopedia/entrypage.html", {
                "query": query,
                "entryPageConent": mark_safe(html_content)
            })

        #   elif query in list_of_entries:
        #     return render(request, "encyclopedia/entrypage.html", {
        #         "query": query,
        #         "searchResult": list_of_entries
        #     })

        else:
            list_of_search_result = []
            # lower_list = [item.lower() for item in list_of_search_result]
            for w in list_of_entries:
                if query in w:
                    list_of_search_result.append(w)
            if list_of_search_result:
                return render(request, "encyclopedia/search.html", {
                    "query": query,
                    "searchResult": list_of_search_result
                    })
            else:
                return render(request, "encyclopedia/error.html", {
                    "message" : "Page does not exist"
                })


            # If entry is not found, render an error page
            # return render(request, "encyclopedia/error.html")

    else:
        # If the request method is GET, render the index page with the list of entries
        entries = util.list_entries()
        return render(request, "encyclopedia/index.html", {
            "query" : "List of entries",
            "entries": entries
        })






def entriesroute(request, entry):
    try:
        entryContent = util.get_entry(entry)
    except UnicodeDecodeError as e:
        # Handle the UnicodeDecodeError
        return render(request, "encyclopedia/error.html", {
                "message": f"Error decoding entry content: {e}."
                })
        # print(entryContent)
    if request.method == 'POST':
        return render(request, "encyclopedia/edit.html",{
            "query": entry,
            "previousContent" : entryContent
        } )
    else:
        if not entryContent:
            return render(request, "encyclopedia/error.html", {
                "message" : "Page does not exist"
            })
        # Converting Markdown content to html    
        html_content = markdown.markdown(entryContent)
        return render(request, "encyclopedia/entrypage.html", {
            "query": entry,
            "entryPageConent" : mark_safe(html_content)
        }) 



def create(request):
    if request.method == 'POST':
        page_title = request.POST.get('title')
        page_content = request.POST.get('message')
        try:
            util.save_entry(page_title, page_content)
        except (IOError, Exception) as e:
            return render(request, "encyclopedia/error.html", {
                    "message" : "Error Saving entry"
                })
        # Retrieve entry containing the page_title string
        entry = util.get_entry(page_title)
        if entry == 'None':
            return render(request, "encyclopedia/error.html", {
                "message": "Entry not found after saving. Please try again."
            })
        else:
            # html_content = markdown.markdown(entry)
            return redirect(f'wiki/{page_title}')
            # return render(request, "encyclopedia/entrypage.html", {
            #     "query": page_title,
            #     "entryPageContent": mark_safe(html_content)
            # })

    else:
        return render (request, "encyclopedia/create.html")


def randomPage(request):
    list_of_entries = util.list_entries()
    random_entry = util.get_entry(random.choice(list_of_entries))
    # random_number = random.randint(0, len(list_of_entries))
    # random_entry = list_of_entries[random_number]
    # print(random_entry)

    html_content = markdown.markdown(random_entry)
    return render(request, "encyclopedia/entrypage.html", {
        "query": random_entry,
        "entryPageConent" : mark_safe(html_content)
    })
    

def editentries(request):
    if request.method == 'POST':
        page_title = request.POST.get("title")
        # or use "request.POST["<name>"]"
        page_content = request.POST.get("message")
        util.save_entry(page_title, page_content)
        return redirect(f'wiki/{page_title}')