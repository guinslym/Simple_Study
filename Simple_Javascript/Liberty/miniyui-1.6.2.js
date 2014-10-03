var miniYUI = {
    version: 1.62,
    dom: {
        //传入参数(对象，className)
        hasClass: function(b, a) {
            //返回类名及其索引值，最小值为0，故结果为true
            return a && ("" + b.className + "").indexOf("" + a + "") > -1;
        },
        addClass: function(b, a) {
            if (b.className === "") {
                b.className = a;
            } else {
                if (b.className !== "" && !this.hasClass(b, a)) {
                    b.className = b.className + " " + a;
                }
            }
        },
        removeClass: function(b, a) {
            if (this.hasClass(b, a)) {
                //将类名是a的取代为空字符串，无论是其开头还是结束的。
                b.className = ("" + b.className + "").replace("" + a + "", "").replace(/^ | $/g, "");
            }
        },
        //传出参数(子节点，类名,父节点)
        getByClassName: function(b,f,c) {
            if (typeof c=='undefined') {
                c=document;
            }
            var d = [];
            if(c.getElementsByClassName){
                var nodes=c.getElementsByClassName(f);
                for (var i = 0,len=nodes.length; i < len; i++) {
                    d.push(nodes.item(i));
                }
                return d;
            }else{
                var g = c.getElementsByTagName(b);
                for (var e = 0, len = g.length; e < len; e++) {
                    if (this.hasClass(g[e], f)) {
                        d[d.length] = g[e];
                        //d.push(g[e]);
                    }
                }
                return d;
            }
        },
        getPreviousSibling: function(a) {
            while (a) {
                a = a.previousSibling;
                if (a && a.nodeType == 1) {
                    return a;
                }
            }
            return null;
        },
        getNextSibling: function(a) {
            while (a) {
                a = a.nextSibling;
                if (a && a.nodeType == 1) {
                    return a;
                }
            }
            return null;
        },
        getChildren: function(e) {
            var b = e.children || e.childNodes,
            c,
            a,
            d = [];
            a = b.length;
            if (a === 0) {
                return d
            }
            if (e.children) {
                return b
            } else {
                for (c = 0; c < a; c++) {
                    if (b[c] && (b[c].nodeType == 3 || (b[c].nodeType == 1 && b[c].parentNode != e))) {
                        continue
                    }
                    d[d.length] = b[c];
                }
            }
            return d;
        },
        //传入子节点及父标签
        getParent: function(d, b, c) {
            var a = d;
            do {
                a = a.parentNode;
            }
            while (a && ((typeof(c) == "undefined" && a.tagName.toLowerCase() != b) || (typeof(c) != "undefined" && (!this.hasClass(a, c) || a.tagName.toLowerCase() != b))) && a.tagName.toLowerCase() != "body");
            return a && ((typeof(c) == "undefined" && a.tagName.toLowerCase() == b) || (typeof(c) != "undefined" && this.hasClass(a, c) && a.tagName.toLowerCase() == b)) ? a: null
        },
        getPosition: function() {
            return document.documentElement.getBoundingClientRect && 
            function(b) {
                var c = b.getBoundingClientRect(),
                a = b.ownerDocument || b.document;
                if (/Safari/i.test(navigator.appVersion)) {
                    return {
                        left: c.left + a.documentElement.scrollLeft,
                        top: c.top + a.documentElement.scrollTop + document.body.scrollTop
                    }
                }
                return {
                    left: c.left + a.documentElement.scrollLeft,
                    top: c.top + a.documentElement.scrollTop
                }
            } || 
            function(b) {
                var a = 0,
                c = 0;
                do {
                    a += b.offsetLeft;
                    c += b.offsetTop
                }
                while ((b = b.offsetParent));
                return {
                    left: a,
                    top: c
                }
            }
        } (),
        isChild: function(b, a) {
            if (!b || !a) {
                return "we need son element object and parent element object.";
            }
            if (a.tagName && a.tagName.toLowerCase() == "body") {
                return true;
            }
            while (b && b.tagName && b.tagName.toLowerCase() != "body") {
                if (b.parentNode == a) {
                    return true;
                }
                b = b.parentNode;
            }
            return false;
        },
        getStyle: function(d, c, a) {
            var b = /(\d+(\.\d+)*)?[a-z%]*/ig;
            if (d.currentStyle) {
                return a ? parseFloat(d.currentStyle[c].replace(b, "$1").replace("", "0")) : d.currentStyle[c]
            } else {
                return a ? parseFloat(window.getComputedStyle(d, null).getPropertyValue(c).replace(b, "$1").replace("", "0")) : window.getComputedStyle(d, null).getPropertyValue(c)
            }
        },
        getWidth: function(a) {
            return this.getStyle(a, "width", true) > 0 ? this.getStyle(a, "width", true) : a.offsetWidth
        },
        getHeight: function(a) {
            return this.getStyle(a, "height", true) > 0 ? this.getStyle(a, "height", true) : a.offsetHeight
        }
    },
    event: {
        stopEvent: function(a) {
            this.stopPropagation(a);
            this.preventDefault(a)
        },
        stopPropagation: function(a) {
            if (a.stopPropagation) {
                a.stopPropagation()
            } else {
                a.cancelBubble = true
            }
        },
        preventDefault: function(a) {
            if (a.preventDefault) {
                a.preventDefault()
            } else {
                a.returnValue = false
            }
        },
        getEvent: function(d, a) {
            var b = d || window.event;
            if (!b) {
                var f = this.getEvent.caller;
                while (f) {
                    b = f.arguments[0];
                    if (b && Event == b.constructor) {
                        break
                    }
                    f = f.caller
                }
            }
            return b
        },
        getTarget: function(c, b) {
            var a = c.target || c.srcElement;
            return this.resolveTextNode(a)
        },
        getRelatedTarget: function(b) {
            var a = b.relatedTarget;
            if (!a) {
                if (b.type == "mouseout") {
                    a = b.toElement
                } else {
                    if (b.type == "mouseover") {
                        a = b.fromElement
                    }
                }
            }
            return this.resolveTextNode(a)
        },
        resolveTextNode: function(b) {
            try {
                if (b && 3 == b.nodeType) {
                    return b.parentNode
                }
            } catch(a) {}
            return b
        },
        getXY: function(a) {
            return {
                x: a.pageX ? a.pageX: a.clientX + document.documentElement.scrollLeft,
                y: a.pageY ? a.pageY: a.clientY + document.documentElement.scrollTop
            }
        },
        on: function() {
            if (window.addEventListener) {
                return function(c, d, b, a) {
                    c.addEventListener(d, b, (a))
                }
            } else {
                if (window.attachEvent) {
                    return function(c, d, b, a) {
                        c.attachEvent("on" + d, b)
                    }
                } else {
                    return function() {}
                }
            }
        } ()
    },
    connection: {
        ajax: {
            xhr: [],
            activeRequestCount: 0,
            Try: {
                these: function() {
                    var c;
                    for (var b = 0, d = arguments.length; b < d; b++) {
                        var a = arguments[b];
                        try {
                            c = a();
                            break
                        } catch(f) {}
                    }
                    return c
                }
            },
            getTransport: function() {
                return this.Try.these(function() {
                    return new XMLHttpRequest()
                },
                function() {
                    return new ActiveXObject("Msxml2.XMLHTTP")
                },
                function() {
                    return new ActiveXObject("Microsoft.XMLHTTP")
                }) || false
            },
            getXHR: function() {
                for (var a = 0; a < this.xhr.length; a++) {
                    if (this.xhr[a].readyState == 0 || this.xhr[a].readyState == 4) {
                        if (this.xhr[a].readyState == 4) {
                            this.xhr[a].abort()
                        }
                        return this.xhr[a]
                    }
                }
                this.xhr[this.xhr.length] = this.getTransport();
                return this.xhr[this.xhr.length - 1]
            }
        },
        asyncRequest: function(a, d, j, b) {
            if (typeof(j) == "undefined") {
                var j = {}
            }
            var h = typeof(b) == "string" ? b: "";
            if (typeof(b) == "object") {
                for (key in b) {
                    h += key + "=" + b[key] + "&"
                }
            }
            h = h.replace(/&$/, "");
            var c = typeof(j.async) != "undefined" ? j.async: true;
            var g = [],
            f = 0;
            var k = this.ajax.getXHR();
            if (!k) {
                return
            }
            var e = function(i) {
                if (typeof(j[i]) == "undefined") {
                    return false
                }
                if (j.argument && j.argument.length > 0) {
                    g[0] = k;
                    for (f = 0; f < j.argument.length; f++) {
                        g[f + 1] = j.argument[f]
                    }
                    j[i].apply(k, g)
                } else {
                    j[i](k)
                }
            };
            k.onreadystatechange = function() {
                if (k.readyState == 4) {
                    if (k.status == 200) {
                        e("success")
                    } else {
                        e("failure")
                    }
                }
            };
            if (!c && (/Firefox/ig).test(navigator.userAgent)) {
                k.onload = function() {
                    e("success")
                }
            }
            if (!j.cache) {
                d += ((d.indexOf("?") == -1) ? "?": "&") + "rnd=" + new Date().valueOf().toString()
            }
            if (a.toUpperCase() == "POST") {
                k.open("POST", encodeURI(d), c);
                k.setRequestHeader("Content-Length", h.length);
                k.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
                k.send(h)
            } else {
                if (a.toUpperCase() == "GET") {
                    d += ((d.indexOf("?") == -1) ? "?": "&") + h;
                    k.open("GET", encodeURI(d), c);
                    k.setRequestHeader("Content-Length", h.length);
                    k.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
                    k.send(null)
                }
            }
        },
        xRequest: function(b, f, e) {
            var a = f || "oscript" + Math.random().toString().replace(/\./g, "");
            var d = document.getElementById(a);
            var c = document.getElementsByTagName("head").item(0);
            if (d && d.parentNode == c) {
                c.removeChild(d)
            }
            d = document.createElement("script");
            d.setAttribute("src", b);
            d.setAttribute("id", a);
            d.setAttribute("type", "text/javascript");
            if (typeof(e) != "undefined") {
                d.setAttribute("charset", e)
            }
            c.appendChild(d);
            return d
        }
    },
    clone: function(b) {
        if (typeof(b) != "object") {
            return null
        }
        var c = {};
        if (!b.length) {
            for (key in b) {
                c[key] = b[key]
            }
        } else {
            c = [];
            for (var a = 0; a < b.length; a++) {
                c[a] = b[a]
            }
        }
        return c
    },
    queue: {
        _timer: null,
        step: 1500,
        list: [],
        add: function(c, d, b) {
            var a = Array.prototype.slice.call(arguments, 3);
            this.list.unshift({
                fn: c,
                step: d,
                scope: b,
                args: a
            })
        },
        run: function() {
            if (this.list.length === 0) {
                return
            }
            var b = this.list.pop();
            b.fn.apply(b.scope, b.args);
            var a = this;
            this._timer = setTimeout(function() {
                a.run()
            },
            b.step > 0 ? b.step: this.step)
        },
        stop: function() {
            if (this._timer) {
                clearTimeout(this._timer)
            }
        }
    },
    doWhileExist: function(c, b) {
        var a = Array.prototype.slice.call(arguments, 2);
        var d = document.getElementById(c);
        if (d) {
            a.unshift(d);
            b.apply(null, a)
        }
    }
};