#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import mypysort

class MainHandler(webapp2.RequestHandler):
    def get(self):
        sort = self.request.GET.get("sort")
        if sort is None:
            self.response.write("You must specify sort array")
            return
        sort = sort.split(",")
        method = self.request.GET.get("method")
        if method is None:
            method = "quick"
        if method == "quick":
            src = mypysort.quick_sort(sort , 0 , len(sort))
        elif method == "bubble":
            src = mypysort.bubble_sort(sort)
        else:
            self.response.write("Method [%s] not support"%method)
            return
        self.response.write(",".join(src))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
