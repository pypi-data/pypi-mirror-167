"use strict";
(self["webpackChunkipylabel"] = self["webpackChunkipylabel"] || []).push([["lib_widgets_js"],{

/***/ "./lib/ReactWidget.js":
/*!****************************!*\
  !*** ./lib/ReactWidget.js ***!
  \****************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.defaultModelProperties = void 0;
const react_1 = __importDefault(__webpack_require__(/*! react */ "webpack/sharing/consume/default/react"));
const widget_model_1 = __webpack_require__(/*! ./hooks/widget-model */ "./lib/hooks/widget-model.js");
const util_1 = __webpack_require__(/*! ./util */ "./lib/util.js");
// widget state, don't forget to update `ipylabel/example.py`
exports.defaultModelProperties = {
    value: "Hello World",
};
function ReactWidget(props) {
    const [name, setName] = (0, widget_model_1.useModelState)("value");
    const inputStyle = {
        padding: "7px",
        background: "whitesmoke",
        border: "1px solid gray",
        borderRadius: "4px",
    };
    return (react_1.default.createElement("div", { className: "Widget" },
        react_1.default.createElement("h1", null,
            "Hello ",
            name),
        react_1.default.createElement("input", { style: inputStyle, type: "text", value: name, onChange: (e) => setName(e.target.value) })));
}
exports["default"] = (0, util_1.withModelContext)(ReactWidget);
//# sourceMappingURL=ReactWidget.js.map

/***/ }),

/***/ "./lib/TextWidget.js":
/*!***************************!*\
  !*** ./lib/TextWidget.js ***!
  \***************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.defaultModelProperties = void 0;
const react_1 = __importStar(__webpack_require__(/*! react */ "webpack/sharing/consume/default/react"));
const widget_model_1 = __webpack_require__(/*! ./hooks/widget-model */ "./lib/hooks/widget-model.js");
const components_1 = __webpack_require__(/*! ./components */ "./lib/components/index.js");
const util_1 = __webpack_require__(/*! ./util */ "./lib/util.js");
// widget state, don't forget to update `ipylabel/text.py`
exports.defaultModelProperties = {
    // use as inputs
    text: "",
    labels: [],
    colors: [],
    // set as outputs
    result: [],
    finished: false,
};
const TextWidget = (props) => {
    // use as input
    const [text] = (0, widget_model_1.useModelState)("text");
    const [labels] = (0, widget_model_1.useModelState)("labels");
    const [colors] = (0, widget_model_1.useModelState)("colors");
    // set as output
    const [result, setResult] = (0, widget_model_1.useModelState)("result");
    const [finished, setFinished] = (0, widget_model_1.useModelState)("finished");
    // values for inner use
    const [selectedLabel, setSelectedLabel] = (0, react_1.useState)(labels[0]);
    const [selectedColor, setSelectedColor] = (0, react_1.useState)(colors[0]);
    const [selection, setSelection] = (0, react_1.useState)(null);
    const label2color = Object.fromEntries(labels.map((label, idx) => [label, colors[idx]]));
    function selections_overlap(first, second) {
        return ((first.start <= second.start && first.end >= second.start) ||
            (first.start >= second.start && first.end <= second.end) ||
            (first.start <= second.end && first.end >= second.end));
    }
    const handleAddClick = () => {
        if (selection !== null) {
            if (result.filter((element) => selections_overlap({ start: element.start, end: element.end }, selection)).length === 0) {
                // dont have overlaps
                setResult(result.concat([
                    {
                        start: selection.start,
                        end: selection.end,
                        label: selectedLabel,
                    },
                ]));
            }
        }
    };
    const handleRemoveClick = () => {
        if (selection !== null) {
            setResult(result.filter((element) => !(selection.start <= element.start && selection.end >= element.end)));
        }
    };
    return (react_1.default.createElement("div", { className: "TextWidget" },
        react_1.default.createElement("div", { className: "flex-column" },
            react_1.default.createElement("div", { className: "flex-row" },
                react_1.default.createElement(components_1.DropDown, { options: labels.map((label, index) => ({
                        text: label,
                        color: colors[index],
                    })), onChange: ({ text, color }) => {
                        setSelectedLabel(text);
                        setSelectedColor(color);
                    }, disabled: finished }),
                react_1.default.createElement(components_1.Button, { label: `Label selected as ${selectedLabel}`, disabled: finished, onClick: handleAddClick, displayColor: selectedColor }),
                react_1.default.createElement(components_1.Checkbox, { value: finished, label: "Nothing to label", onChange: () => setFinished(!finished) }),
                react_1.default.createElement("div", { className: "m-auto" }),
                react_1.default.createElement(components_1.Button, { label: "Remove selected", disabled: finished, onClick: handleRemoveClick }),
                react_1.default.createElement(components_1.Button, { label: "Reset", disabled: finished, onClick: () => setResult([]) })),
            react_1.default.createElement("div", null,
                react_1.default.createElement(components_1.Selectable, { text: text, selected: result, disabled: finished, label2color: label2color, onSelectionChange: setSelection })))));
};
exports["default"] = (0, util_1.withModelContext)(TextWidget);
//# sourceMappingURL=TextWidget.js.map

/***/ }),

/***/ "./lib/components/Button.js":
/*!**********************************!*\
  !*** ./lib/components/Button.js ***!
  \**********************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
const react_1 = __importDefault(__webpack_require__(/*! react */ "webpack/sharing/consume/default/react"));
const Button = ({ label, disabled, onClick, displayColor, }) => {
    return (react_1.default.createElement("button", { disabled: disabled, onClick: onClick },
        react_1.default.createElement("div", { className: "flex-column" },
            react_1.default.createElement("div", { className: "flex-row" },
                label,
                displayColor ? (react_1.default.createElement("span", { style: {
                        background: displayColor,
                        width: "1em",
                        height: "1em",
                        marginLeft: "0.5em",
                    } }, "\u00A0")) : null))));
};
exports["default"] = Button;
//# sourceMappingURL=Button.js.map

/***/ }),

/***/ "./lib/components/Checkbox.js":
/*!************************************!*\
  !*** ./lib/components/Checkbox.js ***!
  \************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
const react_1 = __importDefault(__webpack_require__(/*! react */ "webpack/sharing/consume/default/react"));
const Checkbox = ({ value, label, onChange }) => {
    return (react_1.default.createElement("div", null,
        react_1.default.createElement("label", null,
            react_1.default.createElement("input", { type: "checkbox", checked: value, onChange: onChange }), label !== null && label !== void 0 ? label : label)));
};
exports["default"] = Checkbox;
//# sourceMappingURL=Checkbox.js.map

/***/ }),

/***/ "./lib/components/DropDown.js":
/*!************************************!*\
  !*** ./lib/components/DropDown.js ***!
  \************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
const react_1 = __importStar(__webpack_require__(/*! react */ "webpack/sharing/consume/default/react"));
const DropDown = ({ disabled = false, options, onChange, label, }) => {
    const [selectedText, setSelectedText] = (0, react_1.useState)(options[0].text);
    const [selectedColor, setSelectedColor] = (0, react_1.useState)(options[0].color);
    (0, react_1.useEffect)(() => onChange({ text: selectedText, color: selectedColor }), [selectedColor, selectedText]);
    return (react_1.default.createElement("div", null,
        react_1.default.createElement("label", null,
            react_1.default.createElement("select", { onChange: (event) => {
                    const option = options[parseInt(event.target.value)];
                    setSelectedText(option.text);
                    setSelectedColor(option.color);
                }, disabled: disabled }, options.map((option, index) => (react_1.default.createElement("option", { value: index, key: index }, option.text)))), label !== null && label !== void 0 ? label : label)));
};
exports["default"] = DropDown;
//# sourceMappingURL=DropDown.js.map

/***/ }),

/***/ "./lib/components/Selectable.js":
/*!**************************************!*\
  !*** ./lib/components/Selectable.js ***!
  \**************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
const react_1 = __importDefault(__webpack_require__(/*! react */ "webpack/sharing/consume/default/react"));
const Selectable = ({ text, disabled, selected, label2color, onSelectionChange, }) => {
    const handleSelection = (event) => {
        const selection = window.getSelection();
        const first_end = parseInt(selection.getRangeAt(0).startContainer.parentNode
            .dataset.position);
        const second_end = parseInt(selection.getRangeAt(0).endContainer.parentNode.dataset
            .position);
        let selectionStart, selectionEnd;
        if (first_end < second_end) {
            [selectionStart, selectionEnd] = [first_end, second_end];
        }
        else {
            [selectionStart, selectionEnd] = [second_end, first_end];
        }
        onSelectionChange({ start: selectionStart, end: selectionEnd });
    };
    return (react_1.default.createElement("div", { onMouseUp: handleSelection, onDoubleClick: handleSelection }, text.split("").map((letter, idx) => {
        let label_as = null;
        selected.forEach((element) => {
            if (idx >= element["start"] && idx <= element["end"]) {
                label_as = element["label"];
            }
        });
        if (label_as !== null) {
            return (react_1.default.createElement("abbr", { "data-position": idx, title: label_as, style: { background: disabled ? "none" : label2color[label_as] }, key: idx }, letter));
        }
        else {
            return (react_1.default.createElement("span", { "data-position": idx, key: idx }, letter));
        }
    })));
};
exports["default"] = Selectable;
//# sourceMappingURL=Selectable.js.map

/***/ }),

/***/ "./lib/components/index.js":
/*!*********************************!*\
  !*** ./lib/components/index.js ***!
  \*********************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Selectable = exports.DropDown = exports.Checkbox = exports.Button = void 0;
const Button_1 = __importDefault(__webpack_require__(/*! ./Button */ "./lib/components/Button.js"));
exports.Button = Button_1.default;
const Checkbox_1 = __importDefault(__webpack_require__(/*! ./Checkbox */ "./lib/components/Checkbox.js"));
exports.Checkbox = Checkbox_1.default;
const DropDown_1 = __importDefault(__webpack_require__(/*! ./DropDown */ "./lib/components/DropDown.js"));
exports.DropDown = DropDown_1.default;
const Selectable_1 = __importDefault(__webpack_require__(/*! ./Selectable */ "./lib/components/Selectable.js"));
exports.Selectable = Selectable_1.default;
//# sourceMappingURL=index.js.map

/***/ }),

/***/ "./lib/hooks/widget-model.js":
/*!***********************************!*\
  !*** ./lib/hooks/widget-model.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.useModel = exports.useModelEvent = exports.useModelState = exports.WidgetModelContext = void 0;
const react_1 = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
exports.WidgetModelContext = (0, react_1.createContext)(undefined);
// HOOKS
// =====
/**
 * @param name property name in the Python model object.
 * @returns model state and set state function.
 */
function useModelState(name) {
    const model = useModel();
    const [state, setState] = (0, react_1.useState)(model === null || model === void 0 ? void 0 : model.get(name));
    useModelEvent(`change:${name}`, (model) => {
        setState(model.get(name));
    }, [name]);
    function updateModel(val, options) {
        model === null || model === void 0 ? void 0 : model.set(name, val, options);
        model === null || model === void 0 ? void 0 : model.save_changes();
    }
    return [state, updateModel];
}
exports.useModelState = useModelState;
/**
 * Subscribes a listener to the model event loop.
 * @param event String identifier of the event that will trigger the callback.
 * @param callback Action to perform when event happens.
 * @param deps Dependencies that should be kept up to date within the callback.
 */
function useModelEvent(event, callback, deps) {
    const model = useModel();
    const dependencies = deps === undefined ? [model] : [...deps, model];
    (0, react_1.useEffect)(() => {
        const callbackWrapper = (e) => model && callback(model, e);
        model === null || model === void 0 ? void 0 : model.on(event, callbackWrapper);
        return () => void (model === null || model === void 0 ? void 0 : model.unbind(event, callbackWrapper));
    }, dependencies);
}
exports.useModelEvent = useModelEvent;
/**
 * An escape hatch in case you want full access to the model.
 * @returns Python model
 */
function useModel() {
    return (0, react_1.useContext)(exports.WidgetModelContext);
}
exports.useModel = useModel;
//# sourceMappingURL=widget-model.js.map

/***/ }),

/***/ "./lib/util.js":
/*!*********************!*\
  !*** ./lib/util.js ***!
  \*********************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.withModelContext = void 0;
const react_1 = __importDefault(__webpack_require__(/*! react */ "webpack/sharing/consume/default/react"));
const widget_model_1 = __webpack_require__(/*! ./hooks/widget-model */ "./lib/hooks/widget-model.js");
function withModelContext(Component) {
    return function withModelContext(props) {
        return (react_1.default.createElement(widget_model_1.WidgetModelContext.Provider, { value: props.model },
            react_1.default.createElement(Component, Object.assign({}, props))));
    };
}
exports.withModelContext = withModelContext;
//# sourceMappingURL=util.js.map

/***/ }),

/***/ "./lib/version.js":
/*!************************!*\
  !*** ./lib/version.js ***!
  \************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


// Copyright (c) Danil Kireev
// Distributed under the terms of the Modified BSD License.
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MODULE_NAME = exports.MODULE_VERSION = void 0;
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
// eslint-disable-next-line @typescript-eslint/no-var-requires
const data = __webpack_require__(/*! ../package.json */ "./package.json");
/**
 * The _model_module_version/_view_module_version this package implements.
 *
 * The html widget manager assumes that this is the same as the npm package
 * version number.
 */
exports.MODULE_VERSION = data.version;
/*
 * The current package name.
 */
exports.MODULE_NAME = data.name;
//# sourceMappingURL=version.js.map

/***/ }),

/***/ "./lib/widgets.js":
/*!************************!*\
  !*** ./lib/widgets.js ***!
  \************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


// Copyright (c) Danil Kireev
// Distributed under the terms of the Modified BSD License.
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.TextLabelingView = exports.TextLabelingModel = exports.ExampleView = exports.ExampleModel = void 0;
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const ReactWidget_1 = __importStar(__webpack_require__(/*! ./ReactWidget */ "./lib/ReactWidget.js"));
const TextWidget_1 = __importStar(__webpack_require__(/*! ./TextWidget */ "./lib/TextWidget.js"));
const react_1 = __importDefault(__webpack_require__(/*! react */ "webpack/sharing/consume/default/react"));
const react_dom_1 = __importDefault(__webpack_require__(/*! react-dom */ "webpack/sharing/consume/default/react-dom"));
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
// Import the CSS
__webpack_require__(Object(function webpackMissingModule() { var e = new Error("Cannot find module '../css/widget.css'"); e.code = 'MODULE_NOT_FOUND'; throw e; }()));
class DefaultDOMWidgetModel extends base_1.DOMWidgetModel {
    constructor() {
        super(...arguments);
        this.model_module = version_1.MODULE_NAME;
        this.model_module_version = version_1.MODULE_VERSION;
        this.view_module = version_1.MODULE_NAME; // Set to null if no view
        this.view_module_version = version_1.MODULE_VERSION;
    }
    defaults() {
        return Object.assign(Object.assign(Object.assign({}, super.defaults()), { _model_name: this.model_name, _view_name: this.view_name, _model_module: this.model_module, _model_module_version: this.model_module_version, _view_module: this.view_module, _view_module_version: this.view_module_version }), ReactWidget_1.defaultModelProperties);
    }
}
DefaultDOMWidgetModel.serializers = Object.assign({}, base_1.DOMWidgetModel.serializers);
class DefaultDOMWidgetView extends base_1.DOMWidgetView {
    render() {
        const component = react_1.default.createElement(this.widget, {
            model: this.model,
        });
        react_dom_1.default.render(component, this.el);
    }
}
class ExampleModel extends DefaultDOMWidgetModel {
    constructor() {
        super(...arguments);
        this.model_name = "ExampleModel";
        this.view_name = "ExampleView"; // Set to null if no view
        this.defaultModelProperties = ReactWidget_1.defaultModelProperties;
    }
}
exports.ExampleModel = ExampleModel;
class ExampleView extends DefaultDOMWidgetView {
    constructor() {
        super(...arguments);
        this.widget = ReactWidget_1.default;
    }
}
exports.ExampleView = ExampleView;
class TextLabelingModel extends DefaultDOMWidgetModel {
    constructor() {
        super(...arguments);
        this.model_name = "TextLabelingModel";
        this.view_name = "TextLabelingView";
        this.defaultModelProperties = TextWidget_1.defaultModelProperties;
    }
}
exports.TextLabelingModel = TextLabelingModel;
class TextLabelingView extends DefaultDOMWidgetView {
    constructor() {
        super(...arguments);
        this.widget = TextWidget_1.default;
    }
}
exports.TextLabelingView = TextLabelingView;
//# sourceMappingURL=widgets.js.map

/***/ }),

/***/ "./package.json":
/*!**********************!*\
  !*** ./package.json ***!
  \**********************/
/***/ ((module) => {

module.exports = JSON.parse('{"name":"ipylabel","version":"0.1.6","description":"A Jupyter Widget Library for labeling text.","keywords":["jupyter","jupyterlab","jupyterlab-extension","widgets"],"files":["lib/**/*.js","dist/*.js","css/*.css"],"homepage":"https://github.com/unrndm/ipylabel","bugs":{"url":"https://github.com/unrndm/ipylabel/issues"},"license":"BSD-3-Clause","author":{"name":"Danil Kireev","email":"unrndm@gmail.com"},"main":"lib/index.js","types":"./lib/index.d.ts","repository":{"type":"git","url":"https://github.com/unrndm/ipylabel"},"scripts":{"build":"npm-run-all -s build:lib build:nbextension build:labextension:dev","build:prod":"npm-run-all -s build:lib build:nbextension build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","build:lib":"tsc","build:nbextension":"webpack","clean":"npm-run-all -p clean:*","clean:lib":"rimraf lib","clean:labextension":"rimraf ipylabel/labextension","clean:nbextension":"rimraf ipylabel/nbextension/static/index.js","lint":"eslint . --ext .ts,.tsx --fix","lint:check":"eslint . --ext .ts,.tsx","prepack":"npm-run-all -s build:lib","test":"jest --coverage","watch":"npm-run-all -p watch:*","watch:lib":"tsc -w","watch:nbextension":"webpack --watch --mode=development","watch:labextension":"jupyter labextension watch ."},"dependencies":{"@jupyter-widgets/base":"^1.1.10 || ^2.0.0 || ^3.0.0 || ^4.0.0","react":"^18.2.0","react-dom":"^18.2.0"},"devDependencies":{"@babel/core":"^7.19.0","@babel/preset-env":"^7.19.0","@babel/preset-react":"^7.14.5","@babel/preset-typescript":"^7.14.5","@jupyterlab/builder":"^3.0.0","@phosphor/application":"^1.6.0","@phosphor/widgets":"^1.6.0","@types/jest":"^26.0.0","@types/react":"^18.0.18","@types/react-dom":"^17.0.8","@types/webpack-env":"^1.18.0","@typescript-eslint/eslint-plugin":"^3.6.0","@typescript-eslint/parser":"^3.6.0","acorn":"^7.2.0","babel-loader":"^8.2.2","css-loader":"^3.2.0","eslint":"^7.4.0","eslint-config-prettier":"^6.11.0","eslint-plugin-prettier":"^3.1.4","eslint-plugin-react":"^7.31.8","fs-extra":"^7.0.0","identity-obj-proxy":"^3.0.0","jest":"^26.0.0","mkdirp":"^0.5.1","npm-run-all":"^4.1.3","prettier":"^2.0.5","rimraf":"^2.6.2","source-map-loader":"^1.1.3","style-loader":"^1.0.0","ts-jest":"^26.0.0","ts-loader":"^8.0.0","typescript":"~4.8.3","webpack":"^5.61.0","webpack-cli":"^4.0.0"},"babel":{"presets":["@babel/preset-env","@babel/preset-react","@babel/preset-typescript"]},"jupyterlab":{"extension":"lib/plugin","outputDir":"ipylabel/labextension/","sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}}}}');

/***/ })

}]);
//# sourceMappingURL=lib_widgets_js.a5097111dbca8d2570ef.js.map