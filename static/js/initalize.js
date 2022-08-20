// This is a wrapper script to just load the UI python scripts and call python as needed.
async function run_python_file(file) {
  await pyodide.runPythonAsync(await (await fetch(file)).text());
}
if (window.location.protocol != "https:") {
  if (location.hostname != "localhost" && location.hostname != "127.0.0.1") {
    location.href = location.href.replace("http://", "https://");
  }
}
if (location.hostname == "dev.dk64randomizer.com") {
  var _LTracker = _LTracker || [];
  _LTracker.push({
    logglyKey: "5d3aa1b3-6ef7-4bc3-80ae-778d48a571b0",
    sendConsoleErrors: true,
    tag: "loggly-jslogger",
  });
}
run_python_file("ui/__init__.py");
// Sleep function to run functions after X seconds
async function sleep(seconds, func, args) {
  setTimeout(function () {
    func(...args);
  }, seconds * 1000);
}
function save_text_as_file(text, file) {
  var blob = new Blob([text], { type: "text/plain;charset=utf-8" });
  saveAs(blob, file);
}

window.onerror = function (error) {
  banned_errors_text = [
    '"undefined" is not valid JSON', // Loading up the site without any cookies
    "Unexpected non-whitespace character after JSON at position", // Loading up the site when your cookies reflect a prior version
    "Unexpected non-whitespace character after JSON data at line", // Same as above
    "Unexpected token ; in JSON", // Token Error
  ];
  is_banned = false;
  banned_errors_text.forEach((item) => {
    if (error.toString().toLowerCase().indexOf(item.toLowerCase()) > -1) {
      is_banned = true;
    }
  });
  if (!is_banned) {
    toast_alert(error.toString());
  }
};
function toast_alert(text) {
  try {
    _LTracker.push(text);
  } catch {}
  Toastify({
    text: text,
    duration: 15000,
    close: true,
    gravity: "top",
    position: "right",
    stopOnFocus: true,
    style: {
      background: "#800000",
    },
    onClick: function () {},
  }).showToast();
}
function getFile(file) {
  return $.ajax({
    type: "GET",
    url: file,
    async: false,
  }).responseText;
}
var cosmetics;
document
  .getElementById("music_file")
  .addEventListener("change", function (evt) {
    var fileToLoad = document.getElementById("music_file").files[0];
    var fileReader = new FileReader();
    fileReader.onload = function (fileLoadedEvent) {
      var new_zip = new JSZip();
      new_zip.loadAsync(fileLoadedEvent.target.result).then(function () {
        bgm = [];
        fanfares = [];
        events = [];
        for (var file in new_zip.files) {
          if (file.includes("bgm/") && file.slice(-4) == ".bin") {
            new_zip
              .file(file)
              .async("Uint8Array")
              .then(function (content) {
                bgm.push(content);
              });
          } else if (file.includes("fanfares/") && file.slice(-4) == ".bin") {
            new_zip
              .file(file)
              .async("Uint8Array")
              .then(function (content) {
                fanfares.push(content);
              });
          } else if (file.includes("events/") && file.slice(-4) == ".bin") {
            new_zip
              .file(file)
              .async("Uint8Array")
              .then(function (content) {
                events.push(content);
              });
          }
        }
        cosmetics = { bgm: bgm, fanfares: fanfares, events: events };
      });
    };

    fileReader.readAsArrayBuffer(fileToLoad);
  });

jq = $;

$("#form input").on("input change", function (e) {
  //This would be called if any of the input element has got a change inside the form
  var disabled = $("form").find(":input:disabled").removeAttr("disabled");
  const data = new FormData(document.querySelector("form"));
  disabled.attr("disabled", "disabled");
  const json = Object.fromEntries(data.entries());
  setCookie("saved_settings", JSON.stringify(json), 30);
});
$("#form select").on("change", function (e) {
  //This would be called if any of the input element has got a change inside the form
  var disabled = $("form").find(":input:disabled").removeAttr("disabled");
  const data = new FormData(document.querySelector("form"));
  disabled.attr("disabled", "disabled");
  const json = Object.fromEntries(data.entries());
  setCookie("saved_settings", JSON.stringify(json), 30);
});

function setCookie(name, value, days) {
  var expires = "";
  if (days) {
    var date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || "") + expires + "; path=/; secure";
}
function getCookie(name) {
  var nameEQ = name + "=";
  var ca = document.cookie.split(";");
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == " ") c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
  }
  return null;
}
function eraseCookie(name) {
  document.cookie = name + "=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;";
}

function load_cookies() {
  try {
    if (getCookie("saved_settings") != null) {
      json = JSON.parse(getCookie("saved_settings"));
      if (json !== null) {
        for (var key in json) {
          element = document.getElementsByName(key)[0];
          if (json[key] == "True") {
            element.checked = true;
          } else if (json[key] == "False") {
            element.checked = false;
          }
          try {
            element.value = json[key];
            if (element.hasAttribute("data-slider-value")) {
              element.setAttribute("data-slider-value", json[key]);
            }
          } catch {}
        }
      }
    } else {
      load_presets();
    }
  } catch {
    eraseCookie("saved_settings");
  }
}
load_cookies();
async function load_presets() {
  await pyodide.runPythonAsync(`from ui.rando_options import preset_select_changed
preset_select_changed(None)`);
}

function filebox() {
  var input = document.createElement("input");
  input.type = "file";
  input.accept = ".z64,.n64,.v64";

  input.onchange = (e) => {
    var file = e.target.files[0];
    const reader = new FileReader();

    reader.onload = (event) => {
      // Start a new transaction
      var db = open.result;
      var tx = db.transaction("ROMStorage", "readwrite");
      var store = tx.objectStore("ROMStorage");

      // Add some data
      store.put({ ROM: "N64", value: event.target.result });

      // Close the db when the transaction is done
      tx.oncomplete = function () {
        db.close();
      };
      var getJohn = store.get("N64");
  
      getJohn.onsuccess = function() {
          console.log(getJohn.result);  // => "John"
      };
    };

    reader.readAsBinaryString(file);
  };

  input.click();
}

// This works on all devices/browsers, and uses IndexedDBShim as a final fallback
var indexedDB =
  window.indexedDB ||
  window.mozIndexedDB ||
  window.webkitIndexedDB ||
  window.msIndexedDB ||
  window.shimIndexedDB;

// Open (or create) the database
var open = indexedDB.open("ROMStorage", 1);

// Create the schema
open.onupgradeneeded = function () {
  var db = open.result;
  db.createObjectStore("ROMStorage", { keyPath: "ROM" });
};
