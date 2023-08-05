from genericpath import exists
import os, sys
import tempfile
import shutil

try:
    curr_path = os.path.dirname(os.path.abspath(__file__))
    teedoc_project_path = os.path.abspath(os.path.join(curr_path, "..", "..", ".."))
    if os.path.basename(teedoc_project_path) == "teedoc":
        sys.path.insert(0, teedoc_project_path)
except Exception:
    pass
from teedoc import Plugin_Base
from teedoc import Fake_Logger

__version__ = "1.0.1"


class Plugin(Plugin_Base):
    name = "teedoc_plugin_theme_sakurajimamai"
    desc = "sakurajimamai theme for teedoc"
    defautl_config = {
        "dark": True,
        "default_dark": False,
        "mobile_navbar_collapsed": True,
        "show_print_page": True,
        "toc_depth": 4,
        "env": {
            "main_color": "#4caf7d",
            "sidebar_width": "300px",
            "sidebar_scrollbar_color": "#b8b8b8",
            "toc_depth_str": "h1, h2, h3, h4"
        }
    }

    def on_init(self, config, doc_src_path, site_config, logger=None, multiprocess=True, **kw_args):
        '''
            @config a dict object
            @logger teedoc.logger.Logger object
        '''
        self.logger = Fake_Logger() if not logger else logger
        self.doc_src_path = doc_src_path
        self.site_config = site_config
        self.config = Plugin.defautl_config
        env = self.config["env"]
        if "env" in config:
            env.update(config["env"])
        self.config.update(config)
        self.config["env"] = env
        if self.config["mobile_navbar_collapsed"]:
            self.config["env"]["mobile_navbar_collapsed"] = "none"
        else:
            self.config["env"]["mobile_navbar_collapsed"] = "block"
        if self.config["dark"] and self.config["default_dark"]:
            self.config["env"]["default_theme"] = "dark"
        else:
            self.config["env"]["default_theme"] = "light"
        if self.config["show_print_page"]:
            self.config["env"]["show_print_page"] = "true"
        else:
            self.config["env"]["show_print_page"] = "false"
        if type(self.config["toc_depth"]) != int:
            msg = "-- plugin <{}>'s toc_depth config should be integer, not {}".format(self.name,
                                                                                       self.config["toc_depth"])
            self.logger.e(msg)
            raise Exception(msg)
        if self.config["toc_depth"] < 2:
            self.config["toc_depth"] = 2
        self.config["env"]["toc_depth_str"] = ""
        for i in range(self.config["toc_depth"]):
            self.config["env"]["toc_depth_str"] += f'h{i + 1}, '
        self.config["env"]["toc_depth_str"] = self.config["env"]["toc_depth_str"][:-2]
        self.logger.i("-- plugin <{}> init".format(self.name))
        self.logger.i("-- plugin <{}> config: {}".format(self.name, self.config))
        self.assets_abs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

        self.dark_css = {
            "/static/css/theme_sakurajimamai/dark.css": os.path.join(self.assets_abs_path, "dark.css")
        }
        self.light_css = {
            "/static/css/theme_sakurajimamai/light.css": os.path.join(self.assets_abs_path, "light.css")
        }
        # code hilight css file
        if "code_highlight_css" in self.config and self.config["code_highlight_css"]:
            self.css = {}
            self.code_highlight_css = self.config["code_highlight_css"]
        else:
            self.code_highlight_css = None
            self.css = {
                "/static/css/theme_sakurajimamai/prism.min.css": os.path.join(self.assets_abs_path, "prism.min.css"),
            }
        # image viewer
        self.css["/static/css/theme_sakurajimamai/viewer.min.css"] = os.path.join(self.assets_abs_path,
                                                                                  "viewer.min.css")
        # js files
        self.dark_js = {

        }
        self.light_js = {
        }
        self.header_js = {
            "/static/js/theme_sakurajimamai/split.js": os.path.join(self.assets_abs_path, "split.js"),
            "/static/js/theme_sakurajimamai/jquery.min.js": os.path.join(self.assets_abs_path, "jquery.min.js"),
            "/static/js/theme_sakurajimamai/pre_main.js": os.path.join(self.assets_abs_path, "pre_main.js")
        }
        self.footer_js = {
            "/static/js/theme_sakurajimamai/tocbot.min.js": os.path.join(self.assets_abs_path, "tocbot.min.js"),
            "/static/js/theme_sakurajimamai/main.js": os.path.join(self.assets_abs_path, "main.js"),
            "/static/js/theme_sakurajimamai/viewer.min.js": os.path.join(self.assets_abs_path, "viewer.min.js")
        }
        # code hilight js file
        if "code_highlight_js" in self.config and self.config["code_highlight_js"]:
            self.code_highlight_js = self.config["code_highlight_js"]
        else:
            self.code_highlight_js = None
            self.footer_js["/static/css/theme_sakurajimamai/prism.min.js"] = os.path.join(self.assets_abs_path,
                                                                                          "prism.min.js")
        self.images = {
            "/static/image/theme_sakurajimamai/indicator.svg": os.path.join(self.assets_abs_path, "indicator.svg"),
            "/static/image/theme_sakurajimamai/back.svg": os.path.join(self.assets_abs_path, "back.svg"),
            "/static/image/theme_sakurajimamai/anchor.svg": os.path.join(self.assets_abs_path, "anchor.svg"),
            "/static/image/theme_sakurajimamai/light_menu.svg": os.path.join(self.assets_abs_path, "light_menu.svg"),
            "/static/image/theme_sakurajimamai/dark_menu.svg": os.path.join(self.assets_abs_path, "dark_menu.svg"),
            "/static/image/theme_sakurajimamai/to-top.svg": os.path.join(self.assets_abs_path, "to-top.svg"),
            "/static/image/theme_sakurajimamai/light_mode.svg": os.path.join(self.assets_abs_path, "light_mode.svg"),
            "/static/image/theme_sakurajimamai/dark_mode.svg": os.path.join(self.assets_abs_path, "dark_mode.svg"),
            "/static/image/theme_sakurajimamai/print.svg": os.path.join(self.assets_abs_path, "print.svg")
        }
        # set site_root_url env value
        self.config['env']["site_root_url"] = self.site_config["site_root_url"]
        # replace variable in css with value
        vars = self.config["env"]
        self.temp_dir = os.path.join(tempfile.gettempdir(), "teedoc_plugin_theme_sakurajimamai")
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
        os.makedirs(self.temp_dir)
        self.dark_css = self._update_file_var(self.dark_css, vars, self.temp_dir)
        self.light_css = self._update_file_var(self.light_css, vars, self.temp_dir)
        self.css = self._update_file_var(self.css, vars, self.temp_dir)
        self.header_js = self._update_file_var(self.header_js, vars, self.temp_dir)
        self.footer_js = self._update_file_var(self.footer_js, vars, self.temp_dir)
        # files to copy
        self.html_header_items = self._generate_html_header_items()
        self.files_to_copy = {}
        if self.config["dark"]:
            self.files_to_copy.update(self.dark_css)
            self.files_to_copy.update(self.dark_js)
        self.files_to_copy.update(self.light_css)
        self.files_to_copy.update(self.css)
        self.files_to_copy.update(self.light_js)
        self.files_to_copy.update(self.header_js)
        self.files_to_copy.update(self.footer_js)
        self.files_to_copy.update(self.images)
        if self.config["dark"]:
            self.themes_btn = '<a id="themes" class="light"></a>'
        else:
            self.themes_btn = ""
        self.html_js_items = self._generate_html_js_items()

    def on_del(self):
        if os.path.exists(self.temp_dir):
            try:
                shutil.rmtree(self.temp_dir)
            except Exception:
                pass

    def on_html_template(self, type_name):
        if type_name == "doc":
            return os.path.join(curr_path, "templates", "article.html")
        elif type_name == "page":
            return os.path.join(curr_path, "templates", "page.html")
        elif type_name == "blog":
            return os.path.join(curr_path, "templates", "article.html")
        return None

    def _generate_html_header_items(self):
        items = []
        # css
        for url in self.css:
            item = '<link rel="stylesheet" href="{}" type="text/css"/>'.format(url)
            items.append(item)
        if self.code_highlight_css:
            item = '<link rel="stylesheet" href="{}" type="text/css"/>'.format(self.code_highlight_css)
            items.append(item)
        if self.config["dark"]:
            for url in self.dark_css:
                item = '<link rel="stylesheet" href="{}" type="text/css"/>'.format(url)
                items.append(item)
        for url in self.light_css:
            item = '<link rel="stylesheet" href="{}" type="text/css"/>'.format(url)
            items.append(item)
        if "css" in self.config:
            item = '<link rel="stylesheet" href="{}" type="text/css"/>'.format(self.config["css"])
            items.append(item)
        # header_js
        for url in self.header_js:
            item = '<script src="{}"></script>'.format(url)
            items.append(item)
        if self.config["dark"]:
            for url in self.dark_js:
                item = '<script src="{}"></script>'.format(url)
                items.append(item)
        for url in self.light_js:
            item = '<script src="{}"></script>'.format(url)
            items.append(item)
        return items

    def _generate_html_js_items(self):
        items = []
        for url in self.footer_js:
            item = '<script src="{}"></script>'.format(url)
            items.append(item)
        if "js" in self.config:
            item = '<script src="{}"></script>'.format(self.config["js"])
            items.append(item)
        if self.code_highlight_js:
            item = '<script src="{}"></script>'.format(self.code_highlight_js)
            items.append(item)
        return items

    def _update_file_var(self, files, vars, temp_dir):
        for url, path in files.items():
            with open(path, encoding='utf-8') as f:
                content = f.read()
                for k, v in vars.items():
                    content = content.replace("${}{}{}".format("{", k.strip(), "}"), str(v))
                temp_path = os.path.join(temp_dir, os.path.basename(path))
                with open(temp_path, "w", encoding='utf-8') as fw:
                    fw.write(content)
                files[url] = temp_path
        return files

    def on_add_html_header_items(self, type_name):
        return self.html_header_items

    def on_add_html_footer_js_items(self, type_name):
        return self.html_js_items

    def on_add_navbar_items(self):
        items = [self.themes_btn]
        return items

    def on_copy_files(self):
        res = self.files_to_copy
        self.files_to_copy = {}
        return res


if __name__ == "__main__":
    config = {
    }
    plug = Plugin(config=config)
