#include <Python.h>
#include <structmember.h>

#include <SDL.h>
#include <SDL_opengl.h>

#include <imgui.h>
#include <imgui_impl_sdl.h>
#include <imgui_impl_opengl3.h>

#include <GL/gl.h>

struct MainWindow {
    PyObject_HEAD
    PyObject * size;
    PyObject * ratio;
    PyObject * mouse;
    PyObject * mouse_wheel;
    PyObject * text;
    PyObject * ui;
};

PyTypeObject * MainWindow_type;

SDL_Window * window;
bool closed;
int mouse_x;
int mouse_y;
int mouse_wheel;
bool key_down[280];
bool prev_key_down[280];
char text[1024];

PyObject * keys;
PyObject * empty_str;

MainWindow * meth_main_window(PyObject * self, PyObject * args, PyObject * kwargs) {
    const char * keywords[] = {"size", "title", NULL};

    int width = 1800;
    int height = 960;
    const char * title = "Mollia Window";

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "|(II)s", (char **)keywords, &width, &height, &title)) {
        return NULL;
    }

    if (window) {
        PyErr_Format(PyExc_RuntimeError, "main window already exists");
        return NULL;
    }

    SDL_Init(SDL_INIT_VIDEO | SDL_INIT_TIMER | SDL_INIT_GAMECONTROLLER);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_FLAGS, 0);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 3);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 3);

    SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1);
    SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24);
    SDL_GL_SetAttribute(SDL_GL_STENCIL_SIZE, 8);

    int window_flags = SDL_WINDOW_OPENGL | SDL_WINDOW_ALLOW_HIGHDPI;
    window = SDL_CreateWindow(title, SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, width, height, window_flags);
    SDL_GLContext gl_context = SDL_GL_CreateContext(window);
    SDL_GL_MakeCurrent(window, gl_context);
    SDL_GL_SetSwapInterval(1);

    unsigned char pixels[1024] = {
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0x00,
        0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff,
        0xd4, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0xd4, 0x00, 0x00, 0xff,
        0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff,
        0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0xd4, 0x00, 0x00, 0xff,
        0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff,
        0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0x00, 0xff, 0xff, 0xff, 0x00, 0xff, 0xff, 0xff, 0x00,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0xd4, 0x00, 0x00, 0xff,
        0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff,
        0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0x00, 0xff, 0xff, 0xff, 0x00, 0xff, 0xff, 0xff, 0x00,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0xd4, 0x00, 0x00, 0xff,
        0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff,
        0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0x00, 0xff, 0xff, 0xff, 0x00, 0xff, 0xff, 0xff, 0x00,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0xd4, 0x00, 0x00, 0xff,
        0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff,
        0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0x00, 0xff, 0xff, 0xff, 0x00, 0xff, 0xff, 0xff, 0x00,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0x00,
        0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff, 0xd4, 0x00, 0x00, 0xff,
        0xd4, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff,
        0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0xff,
    };
    SDL_Surface * surface = SDL_CreateRGBSurfaceFrom(pixels, 16, 16, 32, 64, 0xff, 0xff00, 0xff0000, 0xff000000);
    SDL_SetWindowIcon(window, surface);
    SDL_FreeSurface(surface);

    IMGUI_CHECKVERSION();
    ImGui::CreateContext();
    ImGui::StyleColorsDark();
    ImGui::GetStyle().Colors[ImGuiCol_TitleBgActive] = ImGui::GetStyle().Colors[ImGuiCol_TitleBg];
    ImGui::GetStyle().Colors[ImGuiCol_TitleBgCollapsed] = ImGui::GetStyle().Colors[ImGuiCol_TitleBg];
    ImGui::GetStyle().WindowBorderSize = 0.0f;

    ImGuiIO & io = ImGui::GetIO();
    io.IniFilename = NULL;

    ImGui_ImplSDL2_InitForOpenGL(window, gl_context);
    ImGui_ImplOpenGL3_Init("#version 130");

    ImGui_ImplOpenGL3_NewFrame();
    ImGui_ImplSDL2_NewFrame();
    ImGui::NewFrame();

    MainWindow * res = PyObject_New(MainWindow, MainWindow_type);
    res->size = Py_BuildValue("(II)", width, height);
    res->ratio = PyFloat_FromDouble((double)width / (double)height);
    res->mouse = Py_BuildValue("(ii)", 0, 0);
    res->mouse_wheel = PyLong_FromLong(0);
    res->ui = Py_BuildValue("{s{}s{}s{sOs[]ss}s{sOs[]}sO}", "callbacks", "variables", "console", "open", Py_False, "lines", "line", "", "sidebar", "open", Py_False, "content", "tooltip", Py_None);

    Py_INCREF(empty_str);
    res->text = empty_str;

    Py_INCREF(res);
    PyModule_AddObject(self, "wnd", (PyObject *)res);

    return res;
}

PyObject * meth_update(PyObject * self) {
    return PyObject_CallMethod(PyObject_GetAttrString(self, "wnd"), "update", NULL);
}

int sdl_key(int key) {
    switch (key) {
        case SDLK_TAB: return 9;
        case SDLK_LEFT: return 37;
        case SDLK_RIGHT: return 39;
        case SDLK_UP: return 38;
        case SDLK_DOWN: return 40;
        case SDLK_PAGEUP: return 33;
        case SDLK_PAGEDOWN: return 34;
        case SDLK_HOME: return 36;
        case SDLK_END: return 35;
        case SDLK_INSERT: return 45;
        case SDLK_DELETE: return 46;
        case SDLK_BACKSPACE: return 8;
        case SDLK_SPACE: return 32;
        case SDLK_RETURN: return 13;
        case SDLK_ESCAPE: return 27;
        case SDLK_QUOTE: return 222;
        case SDLK_COMMA: return 188;
        case SDLK_MINUS: return 189;
        case SDLK_PERIOD: return 190;
        case SDLK_SLASH: return 191;
        case SDLK_SEMICOLON: return 186;
        case SDLK_EQUALS: return 187;
        case SDLK_LEFTBRACKET: return 219;
        case SDLK_BACKSLASH: return 220;
        case SDLK_RIGHTBRACKET: return 221;
        case SDLK_BACKQUOTE: return 192;
        case SDLK_CAPSLOCK: return 20;
        case SDLK_SCROLLLOCK: return 145;
        case SDLK_NUMLOCKCLEAR: return 144;
        case SDLK_PRINTSCREEN: return 44;
        case SDLK_PAUSE: return 19;
        case SDLK_KP_0: return 96;
        case SDLK_KP_1: return 97;
        case SDLK_KP_2: return 98;
        case SDLK_KP_3: return 99;
        case SDLK_KP_4: return 100;
        case SDLK_KP_5: return 101;
        case SDLK_KP_6: return 102;
        case SDLK_KP_7: return 103;
        case SDLK_KP_8: return 104;
        case SDLK_KP_9: return 105;
        case SDLK_KP_PERIOD: return 110;
        case SDLK_KP_DIVIDE: return 111;
        case SDLK_KP_MULTIPLY: return 106;
        case SDLK_KP_MINUS: return 109;
        case SDLK_KP_PLUS: return 107;
        case SDLK_KP_ENTER: return 269;
        case SDLK_KP_EQUALS: return 160;
        case SDLK_LCTRL: return 162;
        case SDLK_LSHIFT: return 164;
        case SDLK_LALT: return 91;
        case SDLK_LGUI: return 161;
        case SDLK_RCTRL: return 163;
        case SDLK_RSHIFT: return 165;
        case SDLK_RALT: return 92;
        case SDLK_RGUI: return 93;
        case SDLK_0: return 48;
        case SDLK_1: return 49;
        case SDLK_2: return 50;
        case SDLK_3: return 51;
        case SDLK_4: return 52;
        case SDLK_5: return 53;
        case SDLK_6: return 54;
        case SDLK_7: return 55;
        case SDLK_8: return 56;
        case SDLK_9: return 57;
        case SDLK_a: return 65;
        case SDLK_b: return 66;
        case SDLK_c: return 67;
        case SDLK_d: return 68;
        case SDLK_e: return 69;
        case SDLK_f: return 70;
        case SDLK_g: return 71;
        case SDLK_h: return 72;
        case SDLK_i: return 73;
        case SDLK_j: return 74;
        case SDLK_k: return 75;
        case SDLK_l: return 76;
        case SDLK_m: return 77;
        case SDLK_n: return 78;
        case SDLK_o: return 79;
        case SDLK_p: return 80;
        case SDLK_q: return 81;
        case SDLK_r: return 82;
        case SDLK_s: return 83;
        case SDLK_t: return 84;
        case SDLK_u: return 85;
        case SDLK_v: return 86;
        case SDLK_w: return 87;
        case SDLK_x: return 88;
        case SDLK_y: return 89;
        case SDLK_z: return 90;
        case SDLK_F1: return 112;
        case SDLK_F2: return 113;
        case SDLK_F3: return 114;
        case SDLK_F4: return 115;
        case SDLK_F5: return 116;
        case SDLK_F6: return 117;
        case SDLK_F7: return 118;
        case SDLK_F8: return 119;
        case SDLK_F9: return 120;
        case SDLK_F10: return 121;
        case SDLK_F11: return 122;
        case SDLK_F12: return 123;
    }
    return 0;
}

void render_content(PyObject * root, PyObject * callbacks, PyObject * variables, int prefix = 0) {
    PyObject * content = PyDict_GetItemString(root, "content");
    for (int i = 0; i < (int)PyList_Size(content); ++i) {
        switch (prefix) {
            case 1: ImGui::TableNextColumn(); break;
            case 2: if (i) ImGui::SameLine(); break;
        }
        PyObject * obj = PyList_GetItem(content, i);
        PyObject * type = PyDict_GetItemString(obj, "type");
        if (!PyUnicode_CompareWithASCIIString(type, "text")) {
            ImGui::TextUnformatted(PyUnicode_AsUTF8(PyDict_GetItemString(obj, "text")));
            continue;
        }
        if (!PyUnicode_CompareWithASCIIString(type, "button")) {
            if (ImGui::Button(PyUnicode_AsUTF8(PyDict_GetItemString(obj, "text")))) {
                PyObject * click = PyDict_GetItemString(obj, "click");
                PyObject * callback = PyDict_GetItem(callbacks, click);
                Py_XDECREF(PyObject_CallFunction(callback, NULL));
            }
            continue;
        }
        if (!PyUnicode_CompareWithASCIIString(type, "checkbox")) {
            PyObject * variable = PyDict_GetItem(variables, PyDict_GetItemString(obj, "variable"));
            bool value = PyObject_IsTrue(PyDict_GetItemString(variable, "value"));
            if (ImGui::Checkbox(PyUnicode_AsUTF8(PyDict_GetItemString(obj, "text")), &value)) {
                PyDict_SetItemString(variable, "value", value ? Py_True : Py_False);
            }
            continue;
        }
        if (!PyUnicode_CompareWithASCIIString(type, "slider")) {
            PyObject * variable = PyDict_GetItem(variables, PyDict_GetItemString(obj, "variable"));
            PyObject * variable_type = PyDict_GetItemString(variable, "type");
            if (!PyUnicode_CompareWithASCIIString(variable_type, "float")) {
                double value = PyFloat_AsDouble(PyDict_GetItemString(variable, "value"));
                double min_value = PyFloat_AsDouble(PyDict_GetItemString(variable, "min"));
                double max_value = PyFloat_AsDouble(PyDict_GetItemString(variable, "max"));
                const char * format = PyUnicode_AsUTF8(PyDict_GetItemString(obj, "format"));
                if (ImGui::SliderScalar(PyUnicode_AsUTF8(PyDict_GetItemString(obj, "text")), ImGuiDataType_Double, &value, &min_value, &max_value, format)) {
                    PyObject * new_value = PyFloat_FromDouble(value);
                    PyDict_SetItemString(variable, "value", new_value);
                    Py_DECREF(new_value);
                }
                continue;
            }
            if (!PyUnicode_CompareWithASCIIString(variable_type, "int")) {
                int value = PyLong_AsLong(PyDict_GetItemString(variable, "value"));
                int min_value = PyLong_AsLong(PyDict_GetItemString(variable, "min"));
                int max_value = PyLong_AsLong(PyDict_GetItemString(variable, "max"));
                const char * format = PyUnicode_AsUTF8(PyDict_GetItemString(obj, "format"));
                if (ImGui::SliderScalar(PyUnicode_AsUTF8(PyDict_GetItemString(obj, "text")), ImGuiDataType_S32, &value, &min_value, &max_value, format)) {
                    PyObject * new_value = PyLong_FromLong(value);
                    PyDict_SetItemString(variable, "value", new_value);
                    Py_DECREF(new_value);
                }
                continue;
            }
        }
        if (!PyUnicode_CompareWithASCIIString(type, "drag")) {
            PyObject * variable = PyDict_GetItem(variables, PyDict_GetItemString(obj, "variable"));
            PyObject * variable_type = PyDict_GetItemString(variable, "type");
            if (!PyUnicode_CompareWithASCIIString(variable_type, "float")) {
                double value = PyFloat_AsDouble(PyDict_GetItemString(variable, "value"));
                double min_value = PyFloat_AsDouble(PyDict_GetItemString(variable, "min"));
                double max_value = PyFloat_AsDouble(PyDict_GetItemString(variable, "max"));
                float speed = (float)PyFloat_AsDouble(PyDict_GetItemString(obj, "speed"));
                const char * format = PyUnicode_AsUTF8(PyDict_GetItemString(obj, "format"));
                if (ImGui::DragScalar(PyUnicode_AsUTF8(PyDict_GetItemString(obj, "text")), ImGuiDataType_Double, &value, speed, &min_value, &max_value, format)) {
                    PyObject * new_value = PyFloat_FromDouble(value);
                    PyDict_SetItemString(variable, "value", new_value);
                    Py_DECREF(new_value);
                }
                continue;
            }
            if (!PyUnicode_CompareWithASCIIString(variable_type, "int")) {
                int value = PyLong_AsLong(PyDict_GetItemString(variable, "value"));
                int min_value = PyLong_AsLong(PyDict_GetItemString(variable, "min"));
                int max_value = PyLong_AsLong(PyDict_GetItemString(variable, "max"));
                float speed = (float)PyFloat_AsDouble(PyDict_GetItemString(obj, "speed"));
                const char * format = PyUnicode_AsUTF8(PyDict_GetItemString(obj, "format"));
                if (ImGui::DragScalar(PyUnicode_AsUTF8(PyDict_GetItemString(obj, "text")), ImGuiDataType_S32, &value, speed, &min_value, &max_value, format)) {
                    PyObject * new_value = PyLong_FromLong(value);
                    PyDict_SetItemString(variable, "value", new_value);
                    Py_DECREF(new_value);
                }
                continue;
            }
        }
        if (!PyUnicode_CompareWithASCIIString(type, "input")) {
            PyObject * variable = PyDict_GetItem(variables, PyDict_GetItemString(obj, "variable"));
            PyObject * variable_type = PyDict_GetItemString(variable, "type");
            if (!PyUnicode_CompareWithASCIIString(variable_type, "float")) {
                double value = PyFloat_AsDouble(PyDict_GetItemString(variable, "value"));
                double min_value = PyFloat_AsDouble(PyDict_GetItemString(variable, "min"));
                double max_value = PyFloat_AsDouble(PyDict_GetItemString(variable, "max"));
                double step = PyFloat_AsDouble(PyDict_GetItemString(obj, "step"));
                const char * format = PyUnicode_AsUTF8(PyDict_GetItemString(obj, "format"));
                if (ImGui::InputScalar(PyUnicode_AsUTF8(PyDict_GetItemString(obj, "text")), ImGuiDataType_Double, &value, &step, NULL, format)) {
                    value = value > min_value ? value : min_value;
                    value = value < max_value ? value : max_value;
                    PyObject * new_value = PyFloat_FromDouble(value);
                    PyDict_SetItemString(variable, "value", new_value);
                    Py_DECREF(new_value);
                }
                continue;
            }
            if (!PyUnicode_CompareWithASCIIString(variable_type, "int")) {
                int value = PyLong_AsLong(PyDict_GetItemString(variable, "value"));
                int min_value = PyLong_AsLong(PyDict_GetItemString(variable, "min"));
                int max_value = PyLong_AsLong(PyDict_GetItemString(variable, "max"));
                int step = PyLong_AsLong(PyDict_GetItemString(obj, "step"));
                const char * format = PyUnicode_AsUTF8(PyDict_GetItemString(obj, "format"));
                if (ImGui::InputScalar(PyUnicode_AsUTF8(PyDict_GetItemString(obj, "text")), ImGuiDataType_S32, &value, &step, NULL, format)) {
                    value = value > min_value ? value : min_value;
                    value = value < max_value ? value : max_value;
                    PyObject * new_value = PyLong_FromLong(value);
                    PyDict_SetItemString(variable, "value", new_value);
                    Py_DECREF(new_value);
                }
                continue;
            }
        }
        if (!PyUnicode_CompareWithASCIIString(type, "combo")) {
            PyObject * variable = PyDict_GetItem(variables, PyDict_GetItemString(obj, "variable"));
            PyObject * value = PyDict_GetItemString(variable, "value");
            PyObject * options = PyDict_GetItemString(variable, "options");
            int index = (int)PySequence_Index(options, value);
            int num_items = (int)PyList_Size(options);
            const char * items[256];
            for (int i = 0; i < num_items; ++i) {
                items[i] = PyUnicode_AsUTF8(PyList_GetItem(options, i));
            }
            if (ImGui::Combo(PyUnicode_AsUTF8(PyDict_GetItemString(obj, "text")), &index, items, num_items)) {
                PyDict_SetItemString(variable, "value", PyList_GetItem(options, index));
            }
            continue;
        }
        if (!PyUnicode_CompareWithASCIIString(type, "image")) {
            PyObject * callback = PyDict_GetItem(callbacks, PyDict_GetItemString(obj, "texture"));
            int texture = PyLong_AsLong(PyObject_CallFunction(callback, NULL));
            float width = (float)PyFloat_AsDouble(PyDict_GetItemString(obj, "width"));
            float height = (float)PyFloat_AsDouble(PyDict_GetItemString(obj, "height"));
            bool flip = PyObject_IsTrue(PyDict_GetItemString(obj, "flip"));
            int last_texture = 0;
            glGetIntegerv(GL_TEXTURE_BINDING_2D, &last_texture);
            glBindTexture(GL_TEXTURE_2D, texture);
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
            glBindTexture(GL_TEXTURE_2D, last_texture);
            if (flip) {
                ImGui::Image((ImTextureID)(long long)texture, {width, height}, {0.0f, 1.0f}, {1.0f, 0.0f});
            } else {
                ImGui::Image((ImTextureID)(long long)texture, {width, height});
            }
            continue;
        }
        if (!PyUnicode_CompareWithASCIIString(type, "header")) {
            bool open = PyObject_IsTrue(PyDict_GetItemString(obj, "open"));
            ImGui::SetNextItemOpen(open);
            bool next_open = ImGui::CollapsingHeader(PyUnicode_AsUTF8(PyDict_GetItemString(obj, "text")));
            if (next_open) {
                render_content(obj, callbacks, variables);
            }
            if (next_open != open) {
                PyDict_SetItemString(obj, "open", next_open ? Py_True : Py_False);
            }
            continue;
        }
        if (!PyUnicode_CompareWithASCIIString(type, "tree")) {
            bool open = PyObject_IsTrue(PyDict_GetItemString(obj, "open"));
            ImGui::SetNextItemOpen(open);
            bool next_open = ImGui::TreeNode(PyUnicode_AsUTF8(PyDict_GetItemString(obj, "text")));
            if (next_open) {
                render_content(obj, callbacks, variables);
                ImGui::TreePop();
            }
            if (next_open != open) {
                PyDict_SetItemString(obj, "open", next_open ? Py_True : Py_False);
            }
            continue;
        }
        if (!PyUnicode_CompareWithASCIIString(type, "table")) {
            int columns = PyLong_AsLong(PyDict_GetItemString(obj, "columns"));
            if (ImGui::BeginTable("table", columns)) {
                render_content(obj, callbacks, variables, 1);
                ImGui::EndTable();
            }
            continue;
        }
        if (!PyUnicode_CompareWithASCIIString(type, "line")) {
            render_content(obj, callbacks, variables, 2);
            continue;
        }
        if (!PyUnicode_CompareWithASCIIString(type, "separator")) {
            ImGui::Separator();
            continue;
        }
    }
}

PyObject * MainWindow_meth_update(MainWindow * self) {
    if (closed) {
        Py_RETURN_FALSE;
    }

    ImGuiIO & io = ImGui::GetIO();

    PyObject * callbacks = PyDict_GetItemString(self->ui, "callbacks");
    PyObject * variables = PyDict_GetItemString(self->ui, "variables");
    PyObject * console_state = PyDict_GetItemString(self->ui, "console");
    bool console_open = PyObject_IsTrue(PyDict_GetItemString(console_state, "open"));
    ImGui::SetNextWindowPos({0.0f, 0.0f});
    ImGui::SetNextWindowSize({io.DisplaySize.x - 400.0f, 200.0f});
    ImGui::SetNextWindowCollapsed(!console_open);
    bool next_console_open = ImGui::Begin("Console", NULL, ImGuiWindowFlags_NoResize | ImGuiWindowFlags_NoMove);
    if (next_console_open) {
        const float footer_height_to_reserve = ImGui::GetStyle().ItemSpacing.y + ImGui::GetFrameHeightWithSpacing();
        ImGui::BeginChild("scrolling", ImVec2(0.0f, -footer_height_to_reserve), false, ImGuiWindowFlags_HorizontalScrollbar);
        ImGui::PushStyleVar(ImGuiStyleVar_ItemSpacing, ImVec2(4.0f, 1.0f));
        PyObject * lines = PyDict_GetItemString(console_state, "lines");
        for (int i = 0; i < (int)PyList_Size(lines); ++i) {
            PyObject * line = PyList_GetItem(lines, i);
            Py_ssize_t line_length = 0;
            const char * line_str = PyUnicode_AsUTF8AndSize(line, &line_length);
            ImGui::TextUnformatted(line_str, line_str + line_length);
        }
        ImGui::PopStyleVar();

        if (ImGui::GetScrollY() >= ImGui::GetScrollMaxY()) {
            ImGui::SetScrollHereY(1.0f);
        }
        ImGui::EndChild();
        ImGui::Separator();
        char input_buffer[256];
        PyObject * line = PyDict_GetItemString(console_state, "line");
        strcpy(input_buffer, PyUnicode_AsUTF8(line));
        bool reclaim_focus = false;
        ImGuiInputTextFlags input_text_flags = ImGuiInputTextFlags_EnterReturnsTrue;
        ImGui::SetNextItemWidth(-FLT_MIN);
        if (ImGui::InputText("##Input", input_buffer, IM_ARRAYSIZE(input_buffer), input_text_flags, NULL, NULL)) {
            reclaim_focus = true;
            PyObject * callback = PyDict_GetItemString(callbacks, "console_execute");
            Py_XDECREF(PyObject_CallFunction(callback, "(s)", input_buffer));
            PyDict_SetItemString(console_state, "line", empty_str);
        } else if (PyUnicode_CompareWithASCIIString(line, input_buffer)) {
            PyObject * new_line = PyUnicode_FromString(input_buffer);
            PyDict_SetItemString(console_state, "line", new_line);
            Py_DECREF(new_line);
        }

        ImGui::SetItemDefaultFocus();
        if (reclaim_focus) {
            ImGui::SetKeyboardFocusHere(-1);
        }
    }
    ImGui::End();

    PyObject * sidebar_state = PyDict_GetItemString(self->ui, "sidebar");
    bool sidebar_open = PyObject_IsTrue(PyDict_GetItemString(sidebar_state, "open"));
    ImGui::SetNextWindowPos({io.DisplaySize.x - 400.0f, 0.0f});
    ImGui::SetNextWindowSize({400.0f, io.DisplaySize.y});
    ImGui::SetNextWindowCollapsed(!sidebar_open);
    bool next_sidebar_open = ImGui::Begin("Sidebar", NULL, ImGuiWindowFlags_NoResize | ImGuiWindowFlags_NoMove);
    if (next_sidebar_open) {
        render_content(sidebar_state, callbacks, variables);
    }
    ImGui::End();

    PyObject * tooltip = PyDict_GetItemString(self->ui, "tooltip");
    if (tooltip != Py_None) {
        ImGui::BeginTooltip();
        ImGui::PushTextWrapPos(ImGui::GetFontSize() * 35.0f);
        ImGui::TextUnformatted(PyUnicode_AsUTF8(tooltip));
        ImGui::PopTextWrapPos();
        ImGui::EndTooltip();
    }

    if (next_console_open != console_open) {
        PyDict_SetItemString(console_state, "open", next_console_open ? Py_True : Py_False);
    }

    if (next_sidebar_open != sidebar_open) {
        PyDict_SetItemString(sidebar_state, "open", next_sidebar_open ? Py_True : Py_False);
    }

    ImGui::Render();

    if (glIsEnabled(0x8DB9)) {
        glDisable(0x8DB9);
        ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());
        glEnable(0x8DB9);
    } else {
        ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());
    }

    SDL_GL_SwapWindow(window);
    memcpy(prev_key_down, key_down, sizeof(key_down));
    text[0] = 0;

    SDL_Event event;
    while (SDL_PollEvent(&event)) {
        ImGui_ImplSDL2_ProcessEvent(&event);
        if (event.type == SDL_QUIT || (event.type == SDL_WINDOWEVENT && event.window.event == SDL_WINDOWEVENT_CLOSE && event.window.windowID == SDL_GetWindowID(window))) {
            closed = true;
            Py_RETURN_FALSE;
        }
        switch (event.type) {
            case SDL_TEXTINPUT: {
                ImGuiIO & io = ImGui::GetIO();
                if (!io.WantTextInput) {
                    strcat(text, event.text.text);
                }
                break;
            }
            case SDL_KEYDOWN:
            case SDL_KEYUP: {
                ImGuiIO & io = ImGui::GetIO();
                if (!io.WantCaptureKeyboard) {
                    key_down[sdl_key(event.key.keysym.sym)] = event.key.state == SDL_PRESSED;
                }
                break;
            }
            case SDL_MOUSEBUTTONDOWN:
            case SDL_MOUSEBUTTONUP: {
                ImGuiIO & io = ImGui::GetIO();
                if (!io.WantCaptureMouse) {
                    switch (event.button.button) {
                        case SDL_BUTTON_LEFT: key_down[1] = event.button.state == SDL_PRESSED; break;
                        case SDL_BUTTON_RIGHT: key_down[2] = event.button.state == SDL_PRESSED; break;
                        case SDL_BUTTON_MIDDLE: key_down[4] = event.button.state == SDL_PRESSED; break;
                    }
                }
                break;
            }
            case SDL_MOUSEMOTION: {
                ImGuiIO & io = ImGui::GetIO();
                if (!io.WantCaptureMouse) {
                    mouse_x = event.motion.x;
                    mouse_y = event.motion.y;
                }
                break;
            }
            case SDL_MOUSEWHEEL: {
                ImGuiIO & io = ImGui::GetIO();
                if (!io.WantCaptureMouse) {
                    mouse_wheel += event.wheel.y;
                }
                break;
            }
        }
    }

    Py_DECREF(self->mouse);
    Py_DECREF(self->mouse_wheel);
    Py_DECREF(self->text);

    if (text[0]) {
        self->text = PyUnicode_FromString(text);
    } else {
        Py_INCREF(empty_str);
        self->text = empty_str;
    }

    self->mouse = Py_BuildValue("(ii)", mouse_x, mouse_y);
    self->mouse_wheel = PyLong_FromLong(mouse_wheel);

    ImGui_ImplOpenGL3_NewFrame();
    ImGui_ImplSDL2_NewFrame();
    ImGui::NewFrame();
    Py_RETURN_TRUE;
}

int get_key(PyObject * key) {
    if (PyObject * key_code = PyDict_GetItem(keys, key)) {
        return PyLong_AsLong(key_code);
    }
    PyErr_Format(PyExc_ValueError, "no such key %R", key);
    return 0;
}

PyObject * MainWindow_meth_key_pressed(MainWindow * self, PyObject * arg) {
    if (int key = get_key(arg)) {
        if (key_down[key] && !prev_key_down[key]) {
            Py_RETURN_TRUE;
        }
        Py_RETURN_FALSE;
    }
    return NULL;
}

PyObject * MainWindow_meth_key_released(MainWindow * self, PyObject * arg) {
    if (int key = get_key(arg)) {
        if (!key_down[key] && prev_key_down[key]) {
            Py_RETURN_TRUE;
        }
        Py_RETURN_FALSE;
    }
    return NULL;
}

PyObject * MainWindow_meth_key_down(MainWindow * self, PyObject * arg) {
    if (int key = get_key(arg)) {
        if (key_down[key]) {
            Py_RETURN_TRUE;
        }
        Py_RETURN_FALSE;
    }
    return NULL;
}

PyObject * MainWindow_meth_key_up(MainWindow * self, PyObject * arg) {
    if (int key = get_key(arg)) {
        if (!key_down[key]) {
            Py_RETURN_TRUE;
        }
        Py_RETURN_FALSE;
    }
    return NULL;
}

PyObject * MainWindow_meth_demo(MainWindow * self) {
    ImGui::ShowDemoWindow(NULL);
    Py_RETURN_NONE;
}

void default_dealloc(PyObject * self) {
    Py_TYPE(self)->tp_free(self);
}

PyMethodDef MainWindow_methods[] = {
    {"update", (PyCFunction)MainWindow_meth_update, METH_NOARGS, NULL},
    {"key_pressed", (PyCFunction)MainWindow_meth_key_pressed, METH_O, NULL},
    {"key_released", (PyCFunction)MainWindow_meth_key_released, METH_O, NULL},
    {"key_down", (PyCFunction)MainWindow_meth_key_down, METH_O, NULL},
    {"key_up", (PyCFunction)MainWindow_meth_key_up, METH_O, NULL},
    {"demo", (PyCFunction)MainWindow_meth_demo, METH_NOARGS, NULL},
    {},
};

PyMemberDef MainWindow_members[] = {
    {"size", T_OBJECT, offsetof(MainWindow, size), READONLY, NULL},
    {"ratio", T_OBJECT, offsetof(MainWindow, ratio), READONLY, NULL},
    {"mouse", T_OBJECT, offsetof(MainWindow, mouse), READONLY, NULL},
    {"mouse_wheel", T_OBJECT, offsetof(MainWindow, mouse_wheel), READONLY, NULL},
    {"text", T_OBJECT, offsetof(MainWindow, text), READONLY, NULL},
    {"ui", T_OBJECT, offsetof(MainWindow, ui), READONLY, NULL},
    {},
};

PyType_Slot MainWindow_slots[] = {
    {Py_tp_methods, MainWindow_methods},
    {Py_tp_members, MainWindow_members},
    {Py_tp_dealloc, (void *)default_dealloc},
    {},
};

PyType_Spec MainWindow_spec = {"mollia_window.MainWindow", sizeof(MainWindow), 0, Py_TPFLAGS_DEFAULT, MainWindow_slots};

PyMethodDef module_methods[] = {
    {"main_window", (PyCFunction)meth_main_window, METH_VARARGS | METH_KEYWORDS, NULL},
    {"update", (PyCFunction)meth_update, METH_NOARGS, NULL},
    {},
};

PyModuleDef module_def = {PyModuleDef_HEAD_INIT, "mollia_window", NULL, -1, module_methods};

void add_key(const char * name, int code) {
    PyObject * key_code = PyLong_FromLong(code);
    PyDict_SetItemString(keys, name, key_code);
    Py_DECREF(key_code);
}

extern "C" PyObject * PyInit_mollia_window() {
    PyObject * module = PyModule_Create(&module_def);

    MainWindow_type = (PyTypeObject *)PyType_FromSpec(&MainWindow_spec);

    Py_INCREF(MainWindow_type);
    PyModule_AddObject(module, "MainWindow", (PyObject *)MainWindow_type);

    empty_str = PyUnicode_FromString("");
    keys = PyDict_New();

    add_key("mouse1", 1);
    add_key("mouse2", 2);
    add_key("mouse3", 4);
    add_key("tab", 9);
    add_key("left_arrow", 37);
    add_key("right_arrow", 39);
    add_key("up_arrow", 38);
    add_key("down_arrow", 40);
    add_key("pageup", 33);
    add_key("pagedown", 34);
    add_key("home", 36);
    add_key("end", 35);
    add_key("insert", 45);
    add_key("delete", 46);
    add_key("backspace", 8);
    add_key("space", 32);
    add_key("enter", 13);
    add_key("escape", 27);
    add_key("apostrophe", 222);
    add_key("comma", 188);
    add_key("minus", 189);
    add_key("period", 190);
    add_key("slash", 191);
    add_key("semicolon", 186);
    add_key("equal", 187);
    add_key("left_bracket", 219);
    add_key("backslash", 220);
    add_key("right_bracket", 221);
    add_key("graveaccent", 192);
    add_key("capslock", 20);
    add_key("scrolllock", 145);
    add_key("numlock", 144);
    add_key("printscreen", 44);
    add_key("pause", 19);
    add_key("keypad_0", 96);
    add_key("keypad_1", 97);
    add_key("keypad_2", 98);
    add_key("keypad_3", 99);
    add_key("keypad_4", 100);
    add_key("keypad_5", 101);
    add_key("keypad_6", 102);
    add_key("keypad_7", 103);
    add_key("keypad_8", 104);
    add_key("keypad_9", 105);
    add_key("keypad_decimal", 110);
    add_key("keypad_divide", 111);
    add_key("keypad_multiply", 106);
    add_key("keypad_subtract", 109);
    add_key("keypad_add", 107);
    add_key("keypad_enter", 269);
    add_key("left_shift", 160);
    add_key("left_ctrl", 162);
    add_key("left_alt", 164);
    add_key("left_super", 91);
    add_key("right_shift", 161);
    add_key("right_ctrl", 163);
    add_key("right_alt", 165);
    add_key("right_super", 92);
    add_key("menu", 93);
    add_key("0", 48);
    add_key("1", 49);
    add_key("2", 50);
    add_key("3", 51);
    add_key("4", 52);
    add_key("5", 53);
    add_key("6", 54);
    add_key("7", 55);
    add_key("8", 56);
    add_key("9", 57);
    add_key("a", 65);
    add_key("b", 66);
    add_key("c", 67);
    add_key("d", 68);
    add_key("e", 69);
    add_key("f", 70);
    add_key("g", 71);
    add_key("h", 72);
    add_key("i", 73);
    add_key("j", 74);
    add_key("k", 75);
    add_key("l", 76);
    add_key("m", 77);
    add_key("n", 78);
    add_key("o", 79);
    add_key("p", 80);
    add_key("q", 81);
    add_key("r", 82);
    add_key("s", 83);
    add_key("t", 84);
    add_key("u", 85);
    add_key("v", 86);
    add_key("w", 87);
    add_key("x", 88);
    add_key("y", 89);
    add_key("z", 90);
    add_key("f1", 112);
    add_key("f2", 113);
    add_key("f3", 114);
    add_key("f4", 115);
    add_key("f5", 116);
    add_key("f6", 117);
    add_key("f7", 118);
    add_key("f8", 119);
    add_key("f9", 120);
    add_key("f10", 121);
    add_key("f11", 122);
    add_key("f12", 123);

    Py_INCREF(keys);
    PyModule_AddObject(module, "keys", keys);

    Py_INCREF(Py_None);
    PyModule_AddObject(module, "wnd", Py_None);
    return module;
}
