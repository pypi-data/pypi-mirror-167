"use strict";
(self["webpackChunk_jupyterlab_scheduler"] = self["webpackChunk_jupyterlab_scheduler"] || []).push([["lib_index_js"],{

/***/ "./lib/components/environment-picker.js":
/*!**********************************************!*\
  !*** ./lib/components/environment-picker.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "EnvironmentPicker": () => (/* binding */ EnvironmentPicker)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _hooks__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../hooks */ "./lib/hooks.js");


function EnvironmentPicker(props) {
    const [environmentList, setEnvironmentList] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)([]);
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_1__.useTranslator)('jupyterlab');
    react__WEBPACK_IMPORTED_MODULE_0___default().useEffect(() => {
        props.environmentsPromise.then(envList => setEnvironmentList(envList));
    }, []);
    if (environmentList.length === 0) {
        return react__WEBPACK_IMPORTED_MODULE_0___default().createElement("em", null, trans.__('Loading …'));
    }
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("select", { name: props.name, id: props.id, onChange: props.onChange, value: props.initialValue },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("option", { value: "", title: trans.__('No environment selected'), disabled: true }),
        environmentList.map((env, idx) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("option", { value: env.label, title: env.description, key: idx }, env.name)))));
}


/***/ }),

/***/ "./lib/components/icons.js":
/*!*********************************!*\
  !*** ./lib/components/icons.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "calendarAddOnIcon": () => (/* binding */ calendarAddOnIcon),
/* harmony export */   "calendarMonthIcon": () => (/* binding */ calendarMonthIcon),
/* harmony export */   "eventNoteIcon": () => (/* binding */ eventNoteIcon),
/* harmony export */   "replayIcon": () => (/* binding */ replayIcon)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _style_icons_calendar_add_on_svg__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../style/icons/calendar-add-on.svg */ "./style/icons/calendar-add-on.svg");
/* harmony import */ var _style_icons_calendar_month_svg__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../style/icons/calendar-month.svg */ "./style/icons/calendar-month.svg");
/* harmony import */ var _style_icons_event_note_svg__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../style/icons/event-note.svg */ "./style/icons/event-note.svg");
/* harmony import */ var _style_icons_replay_svg__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../../style/icons/replay.svg */ "./style/icons/replay.svg");
// This file is based on iconimports.ts in @jupyterlab/ui-components, but is manually generated.





const calendarAddOnIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'jupyterlab-scheduler:calendar-add-on',
    svgstr: _style_icons_calendar_add_on_svg__WEBPACK_IMPORTED_MODULE_1__["default"]
});
const calendarMonthIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'jupyterlab-scheduler:calendar-month',
    svgstr: _style_icons_calendar_month_svg__WEBPACK_IMPORTED_MODULE_2__["default"]
});
const eventNoteIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'jupyterlab-scheduler:event-note',
    svgstr: _style_icons_event_note_svg__WEBPACK_IMPORTED_MODULE_3__["default"]
});
const replayIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'jupyterlab-scheduler:replay',
    svgstr: _style_icons_replay_svg__WEBPACK_IMPORTED_MODULE_4__["default"]
});


/***/ }),

/***/ "./lib/components/job-details.js":
/*!***************************************!*\
  !*** ./lib/components/job-details.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "JobDetails": () => (/* binding */ JobDetails)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _hooks__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../hooks */ "./lib/hooks.js");


const rowClass = 'jp-notebook-job-details-row';
const keyClass = 'jp-notebook-job-details-key';
const valueClass = 'jp-notebook-job-details-value';
function JobParameters(props) {
    if (props.job.parameters === undefined || props.job.parameters === null) {
        return null;
    }
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_1__.useTranslator)('jupyterlab');
    const params = props.job.parameters;
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: rowClass },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: keyClass }, trans.__('Parameters')),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: valueClass }, Object.keys(params).map((paramName, idx) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: 'jp-notebook-job-parameter', key: idx },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: 'jp-notebook-job-parameter-name', style: { fontWeight: 'bold' } },
                paramName,
                ":",
                ' '),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: 'jp-notebook-job-parameter-value' }, params[paramName])))))));
}
function OutputFormats(props) {
    if (props.job.output_formats === undefined ||
        props.job.output_formats === null) {
        return null;
    }
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_1__.useTranslator)('jupyterlab');
    const outputFormats = props.job.output_formats;
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: rowClass },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: keyClass }, trans.__('Output Formats')),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: valueClass }, outputFormats.join(', '))));
}
function JobDetails(props) {
    if (props.job === null) {
        return null;
    }
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_1__.useTranslator)('jupyterlab');
    const start_date = props.job.start_time
        ? new Date(props.job.start_time)
        : null;
    const start_display_date = start_date
        ? start_date.toLocaleString()
        : null;
    const end_date = props.job.end_time
        ? new Date(props.job.end_time)
        : null;
    const end_display_date = end_date
        ? end_date.toLocaleString()
        : null;
    if (!props.isVisible) {
        return react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "jp-notebook-job-details details-hidden" });
    }
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "jp-notebook-job-details details-visible" },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: 'jp-notebook-job-details-grid' },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: rowClass },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: keyClass }, trans.__('ID')),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: valueClass }, props.job.job_id))),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: 'jp-notebook-job-details-grid' },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: rowClass },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: keyClass }, trans.__('Start date')),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: valueClass }, start_display_date)),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: rowClass },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: keyClass }, trans.__('End date')),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: valueClass }, end_display_date))),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: 'jp-notebook-job-details-grid' },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: rowClass },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: keyClass }, trans.__('Environment')),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: valueClass }, props.job.runtime_environment_name)),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(JobParameters, { job: props.job }),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(OutputFormats, { job: props.job }))));
}


/***/ }),

/***/ "./lib/components/job-row.js":
/*!***********************************!*\
  !*** ./lib/components/job-row.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "JobRow": () => (/* binding */ JobRow)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _hooks__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../hooks */ "./lib/hooks.js");
/* harmony import */ var _icons__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./icons */ "./lib/components/icons.js");
/* harmony import */ var _job_details__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./job-details */ "./lib/components/job-details.js");
/* harmony import */ var _output_format_picker__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./output-format-picker */ "./lib/components/output-format-picker.js");








function get_file_from_path(path) {
    return _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PathExt.basename(path);
}
function StopButton(props) {
    if (props.job.status !== 'IN_PROGRESS') {
        return null;
    }
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_4__.useTranslator)('jupyterlab');
    const buttonTitle = props.job.name
        ? trans.__('Stop "%1"', props.job.name)
        : trans.__('Stop job');
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ToolbarButtonComponent, { onClick: props.clickHandler, tooltip: buttonTitle, icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.stopIcon }));
}
function DeleteButton(props) {
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_4__.useTranslator)('jupyterlab');
    const buttonTitle = props.job.name
        ? trans.__('Delete "%1"', props.job.name)
        : trans.__('Delete job');
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ToolbarButtonComponent, { onClick: props.clickHandler, tooltip: buttonTitle, icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.closeIcon }));
}
function RefillButton(props) {
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_4__.useTranslator)('jupyterlab');
    const buttonTitle = props.job.name
        ? trans.__('Rerun "%1" …', props.job.name)
        : trans.__('Rerun job …');
    // Convert the hash of parameters to an array.
    const jobParameters = props.job.parameters
        ? Object.keys(props.job.parameters).map(key => {
            return { name: key, value: props.job.parameters[key] };
        })
        : undefined;
    const clickHandler = () => {
        var _a;
        let initialState = {
            inputFile: props.job.input_uri,
            jobName: (_a = props.job.name) !== null && _a !== void 0 ? _a : '',
            outputPath: props.job.output_prefix,
            environment: props.job.runtime_environment_name,
            parameters: jobParameters
        };
        // Convert the list of output formats, if any, into a list for the initial state
        const jobOutputFormats = props.job.output_formats;
        const outputFormats = (0,_output_format_picker__WEBPACK_IMPORTED_MODULE_5__.outputFormatsForEnvironment)(props.job.runtime_environment_name);
        if (jobOutputFormats && outputFormats) {
            initialState.outputFormats = outputFormats.filter(of => jobOutputFormats.some(jof => of.name == jof));
        }
        // Switch the view to the form.
        props.showCreateJob();
        props.signal.emit(initialState);
    };
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ToolbarButtonComponent, { onClick: clickHandler, tooltip: buttonTitle, icon: _icons__WEBPACK_IMPORTED_MODULE_6__.replayIcon }));
}
function Timestamp(props) {
    const start_date = props.job.start_time
        ? new Date(props.job.start_time)
        : null;
    const start_display_date = start_date
        ? start_date.toLocaleString()
        : null;
    return react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null, start_display_date);
}
function OutputFiles(props) {
    if (props.job.status !== 'COMPLETED') {
        return null;
    }
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_4__.useTranslator)('jupyterlab');
    // Get all output files.
    const outputTypes = props.job.output_formats || ['ipynb'];
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null, outputTypes.map(outputType => {
        // Compose a specific link.
        const outputName = props.job.output_uri.replace(/ipynb$/, outputType);
        return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("a", { key: outputType, href: `/lab/tree/${outputName}`, title: trans.__('Open "%1"', outputName), onClick: e => props.openOnClick(e, outputName), style: { paddingRight: '1em' } }, outputType));
    })));
}
// Add a row for a job, with columns for each of its traits and a details view below.
function JobRow(props) {
    const [detailsVisible, setDetailsVisible] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(false);
    const job = props.job;
    const rowClass = props.rowClass;
    const cellClass = props.cellClass;
    const detailsVisibleClass = 'details-visible';
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_4__.useTranslator)('jupyterlab');
    const input_relative_uri = job.input_uri;
    const output_relative_uri = job.output_uri;
    // Truncate the path to its filename.
    const input_file = get_file_from_path(job.input_uri);
    const openFileClickHandler = (e, output_uri) => {
        e.preventDefault();
        props.app.commands.execute('docmanager:open', { path: output_uri });
    };
    const openDetailsClickHandler = () => {
        setDetailsVisible(!detailsVisible);
    };
    const translatedStatus = (status) => {
        // This may look inefficient, but it's intended to call the `trans` function
        // with distinct, static values, so that code analyzers can pick up all the
        // needed source strings.
        switch (status) {
            case 'COMPLETED':
                return trans.__('Completed');
            case 'FAILED':
                return trans.__('Failed');
            case 'IN_PROGRESS':
                return trans.__('In progress');
            case 'STOPPED':
                return trans.__('Stopped');
            case 'STOPPING':
                return trans.__('Stopping');
        }
    };
    const viewJobDetailsTitle = job.name
        ? trans.__('View details for "%1"', job.name)
        : trans.__('View job details');
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: rowClass + (detailsVisible ? ' ' + detailsVisibleClass : ''), id: `${rowClass}-${job.job_id}`, "data-job-id": job.job_id },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: cellClass },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("a", { className: "jp-notebook-job-name", onClick: openDetailsClickHandler, title: viewJobDetailsTitle }, job.name || react__WEBPACK_IMPORTED_MODULE_0___default().createElement("em", null, trans.__('unnamed')))),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: cellClass },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("a", { href: `/lab/tree/${input_relative_uri}`, title: trans.__('Open "%1"', input_relative_uri), onClick: e => openFileClickHandler(e, input_relative_uri) }, input_file)),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: cellClass },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(OutputFiles, { job: job, openOnClick: openFileClickHandler, outputUri: output_relative_uri })),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: cellClass },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(Timestamp, { job: job })),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: cellClass }, translatedStatus(job.status)),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: cellClass },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(StopButton, { job: job, clickHandler: () => props.app.commands.execute('scheduling:stop-job', {
                        id: job.job_id
                    }) }),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(DeleteButton, { job: job, clickHandler: () => {
                        props.app.commands.execute('scheduling:delete-job', {
                            id: job.job_id
                        });
                        const jobContainer = document.getElementById(`${rowClass}-${job.job_id}`);
                        jobContainer === null || jobContainer === void 0 ? void 0 : jobContainer.classList.add(`${rowClass}-deleted`);
                    } }),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(RefillButton, { job: job, signal: props.createJobFormSignal, showCreateJob: props.showCreateJob }))),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_job_details__WEBPACK_IMPORTED_MODULE_7__.JobDetails, { job: job, isVisible: detailsVisible })));
}


/***/ }),

/***/ "./lib/components/notebook-jobs-list.js":
/*!**********************************************!*\
  !*** ./lib/components/notebook-jobs-list.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "JobListPageSize": () => (/* binding */ JobListPageSize),
/* harmony export */   "NotebookJobsList": () => (/* binding */ NotebookJobsList),
/* harmony export */   "NotebookJobsListBody": () => (/* binding */ NotebookJobsListBody)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _hooks__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../hooks */ "./lib/hooks.js");
/* harmony import */ var _job_row__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./job-row */ "./lib/components/job-row.js");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../handler */ "./lib/handler.js");





const ListItemClass = 'jp-notebook-job-list-item';
const JobListPageSize = 25;
// Used for table cells including headers
const jobTraitClass = 'jp-notebook-job-list-trait';
function NotebookJobsListBody(props) {
    const [notebookJobs, setNotebookJobs] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(undefined);
    const [jobsQuery, setJobsQuery] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)({});
    const fetchInitialRows = () => {
        // Get initial job list (next_token is undefined)
        props.getJobs(jobsQuery).then(initialNotebookJobs => {
            setNotebookJobs(initialNotebookJobs);
        });
    };
    // Fetch the initial rows asynchronously on component creation
    // After setJobsQuery is called, force a reload.
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => fetchInitialRows(), [jobsQuery]);
    const fetchMoreRows = async (next_token) => {
        // Apply the custom token to the existing query parameters
        const newNotebookJobs = await props.getJobs(Object.assign(Object.assign({}, jobsQuery), { next_token }));
        if (!newNotebookJobs) {
            return;
        }
        // Merge the two lists of jobs and keep the next token from the new response.
        setNotebookJobs({
            jobs: [...((notebookJobs === null || notebookJobs === void 0 ? void 0 : notebookJobs.jobs) || []), ...((newNotebookJobs === null || newNotebookJobs === void 0 ? void 0 : newNotebookJobs.jobs) || [])],
            next_token: newNotebookJobs.next_token
        });
    };
    const reloadButton = (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.Button, { onClick: () => fetchInitialRows() }, "Reload"));
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_2__.useTranslator)('jupyterlab');
    if (notebookJobs === undefined) {
        return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", null,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("em", null, trans.__('Loading …'))));
    }
    if (!(notebookJobs === null || notebookJobs === void 0 ? void 0 : notebookJobs.jobs.length)) {
        return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null,
            reloadButton,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: 'jp-notebook-job-list-empty' }, trans.__('There are no scheduled jobs. ' +
                'Right-click on a file in the file browser to run or schedule a notebook.'))));
    }
    // Display column headers with sort indicators.
    const columns = [
        {
            sortField: 'name',
            name: trans.__('Job name')
        },
        {
            sortField: 'input_uri',
            name: trans.__('Input file')
        },
        {
            sortField: null,
            name: trans.__('Output files')
        },
        {
            sortField: 'start_time',
            name: trans.__('Start time')
        },
        {
            sortField: 'status',
            name: trans.__('Status')
        },
        {
            sortField: null,
            name: trans.__('Actions')
        }
    ];
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null,
        reloadButton,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: `${ListItemClass} jp-notebook-job-list-header` }, columns.map((column, idx) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(NotebookJobsColumnHeader, { key: idx, gridColumn: column, jobsQuery: jobsQuery, setJobsQuery: setJobsQuery })))),
        notebookJobs.jobs.map(job => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_job_row__WEBPACK_IMPORTED_MODULE_3__.JobRow, { key: job.job_id, job: job, createJobFormSignal: props.createJobFormSignal, rowClass: ListItemClass, cellClass: jobTraitClass, app: props.app, showCreateJob: props.showCreateJob }))),
        notebookJobs.next_token && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.Button, { onClick: (e) => fetchMoreRows(notebookJobs.next_token) }, trans.__('Show more')))));
}
const sortAscendingIcon = (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.LabIcon.resolveReact, { icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.caretUpIcon, tag: "span" }));
const sortDescendingIcon = (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.LabIcon.resolveReact, { icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.caretDownIcon, tag: "span" }));
function NotebookJobsColumnHeader(props) {
    const sort = props.jobsQuery.sort_by;
    const defaultSort = sort === null || sort === void 0 ? void 0 : sort[0];
    const headerIsDefaultSort = defaultSort && defaultSort.name === props.gridColumn.sortField;
    const isSortedAscending = headerIsDefaultSort &&
        defaultSort.direction === _handler__WEBPACK_IMPORTED_MODULE_4__.Scheduler.SortDirection.ASC;
    const isSortedDescending = headerIsDefaultSort &&
        defaultSort.direction === _handler__WEBPACK_IMPORTED_MODULE_4__.Scheduler.SortDirection.DESC;
    const sortByThisColumn = () => {
        // If this field is not sortable, do nothing.
        if (!props.gridColumn.sortField) {
            return;
        }
        // Change the sort of this column.
        // If not sorted at all or if sorted descending, sort ascending. If sorted ascending, sort descending.
        let newSortDirection = isSortedAscending
            ? _handler__WEBPACK_IMPORTED_MODULE_4__.Scheduler.SortDirection.DESC
            : _handler__WEBPACK_IMPORTED_MODULE_4__.Scheduler.SortDirection.ASC;
        // Set the new sort direction.
        const newSort = {
            name: props.gridColumn.sortField,
            direction: newSortDirection
        };
        // If this field is already present in the sort list, remove it.
        const oldSortList = sort || [];
        const newSortList = [
            newSort,
            ...oldSortList.filter(item => item.name !== props.gridColumn.sortField)
        ];
        // Sub the new sort list in to the query.
        props.setJobsQuery(Object.assign(Object.assign({}, props.jobsQuery), { sort_by: newSortList }));
    };
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: jobTraitClass, onClick: sortByThisColumn },
        props.gridColumn.name,
        isSortedAscending && sortAscendingIcon,
        isSortedDescending && sortDescendingIcon));
}
function getJobs(jobQuery) {
    const api = new _handler__WEBPACK_IMPORTED_MODULE_4__.SchedulerService({});
    // Impose max_items if not otherwise specified.
    if (!jobQuery.hasOwnProperty('max_items')) {
        jobQuery.max_items = JobListPageSize;
    }
    return api.getJobs(jobQuery);
}
function NotebookJobsList(props) {
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_2__.useTranslator)('jupyterlab');
    const header = react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h1", null, trans.__('Notebook Job Runs'));
    // Retrieve the initial jobs list
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: 'jp-notebook-job-list' },
        header,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(NotebookJobsListBody, { showHeaders: true, createJobFormSignal: props.createJobFormSignal, app: props.app, showCreateJob: props.showCreateJob, getJobs: getJobs })));
}


/***/ }),

/***/ "./lib/components/notebook-jobs-navigation-tab-list.js":
/*!*************************************************************!*\
  !*** ./lib/components/notebook-jobs-navigation-tab-list.js ***!
  \*************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "NotebookJobsNavigationTabList": () => (/* binding */ NotebookJobsNavigationTabList)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _hooks__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../hooks */ "./lib/hooks.js");
/* harmony import */ var _notebook_jobs_navigation_tab__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./notebook-jobs-navigation-tab */ "./lib/components/notebook-jobs-navigation-tab.js");



function NotebookJobsNavigationTabList(props) {
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_1__.useTranslator)('jupyterlab');
    const viewToTitle = {
        JobsList: trans.__('Jobs List'),
        CreateJobForm: trans.__('Create Job')
    };
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("ul", { className: "jp-notebook-job-navigation" }, props.views.map(view => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_notebook_jobs_navigation_tab__WEBPACK_IMPORTED_MODULE_2__.NotebookJobsNavigationTab, { key: view, id: view, onClick: event => props.onTabClick(event, view), title: viewToTitle[view], active: view === props.currentView })))));
}


/***/ }),

/***/ "./lib/components/notebook-jobs-navigation-tab.js":
/*!********************************************************!*\
  !*** ./lib/components/notebook-jobs-navigation-tab.js ***!
  \********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "NotebookJobsNavigationTab": () => (/* binding */ NotebookJobsNavigationTab)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);

function NotebookJobsNavigationTab(props) {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("li", { id: props.id, className: 'jp-notebook-job-navigation-tab' + (props.active ? ' active' : ''), onClick: props.active ? () => { } : e => props.onClick(e, props.id) },
        props.title,
        " Piyush"));
}


/***/ }),

/***/ "./lib/components/notebook-jobs-navigation.js":
/*!****************************************************!*\
  !*** ./lib/components/notebook-jobs-navigation.js ***!
  \****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "NotebookJobsNavigation": () => (/* binding */ NotebookJobsNavigation)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _notebook_jobs_navigation_tab_list__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./notebook-jobs-navigation-tab-list */ "./lib/components/notebook-jobs-navigation-tab-list.js");


function NotebookJobsNavigation(props) {
    const views = ['JobsList', 'CreateJobForm'];
    const setView = (event, view) => {
        if (view === 'JobsList') {
            let initialState = {
                inputFile: '',
                jobName: '',
                outputPath: '',
                environment: '',
                parameters: undefined
            };
            props.toggleSignal.emit(initialState);
        }
        props.toggleFunction();
    };
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_notebook_jobs_navigation_tab_list__WEBPACK_IMPORTED_MODULE_1__.NotebookJobsNavigationTabList, { onTabClick: setView, views: views, currentView: props.currentView }));
}


/***/ }),

/***/ "./lib/components/output-format-picker.js":
/*!************************************************!*\
  !*** ./lib/components/output-format-picker.js ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "OutputFormatPicker": () => (/* binding */ OutputFormatPicker),
/* harmony export */   "outputFormatsForEnvironment": () => (/* binding */ outputFormatsForEnvironment)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);

function outputFormatsForEnvironment(environment) {
    // Retrieve the environment data from session storage.
    const environmentsData = sessionStorage.getItem('environments');
    if (environmentsData === null) {
        return null;
    }
    const environments = JSON.parse(environmentsData);
    const environmentObj = environments.find(env => env.name === environment);
    if (!environmentObj || !environmentObj['output_formats']) {
        return null;
    }
    return environmentObj['output_formats'];
}
function OutputFormatPicker(props) {
    const outputFormats = (0,react__WEBPACK_IMPORTED_MODULE_0__.useMemo)(() => outputFormatsForEnvironment(props.environment), [props.environment]);
    if (outputFormats === null) {
        return null;
    }
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: props.rowClassName },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("label", { className: props.labelClassName }, "Output formats"),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: props.inputClassName },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("ul", { className: "jp-notebook-job-output-formats-options" }, outputFormats.map((of, idx) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("li", { key: idx },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("label", null,
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("input", { type: "checkbox", id: `${props.id}-${of.name}`, value: of.name, onChange: props.onChange, checked: props.value.some(sof => of.name === sof.name) }),
                    ' ',
                    of.label))))))));
}


/***/ }),

/***/ "./lib/components/running-jobs-indicator.js":
/*!**************************************************!*\
  !*** ./lib/components/running-jobs-indicator.js ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "RunningJobsIndicator": () => (/* binding */ RunningJobsIndicator),
/* harmony export */   "RunningJobsIndicatorComponent": () => (/* binding */ RunningJobsIndicatorComponent)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/statusbar */ "webpack/sharing/consume/default/@jupyterlab/statusbar");
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _icons__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./icons */ "./lib/components/icons.js");
/* harmony import */ var _hooks__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../hooks */ "./lib/hooks.js");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__);






function RunningJobsIndicatorComponent(props) {
    const runningJobs = props.runningJobs;
    // Don't display a status bar indicator if there are no running jobs (0 or undefined).
    if (!runningJobs) {
        return null;
    }
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_4__.useTranslator)('jupyterlab');
    const itemTitle = runningJobs > 1
        ? trans.__('%1 jobs running', runningJobs)
        : trans.__('%1 job running', runningJobs);
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_2__.interactiveItem, style: { paddingLeft: '4px', paddingRight: '4px' } },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_2__.GroupItem, { spacing: 4, title: itemTitle, onClick: props.handleClick },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_2__.TextItem, { source: `${runningJobs}` }),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.LabIcon.resolveReact, { icon: _icons__WEBPACK_IMPORTED_MODULE_5__.calendarMonthIcon, tag: "span" }))));
}
function RunningJobsIndicator(props) {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.UseSignal, { signal: props.model.inProgressJobCountChanged }, (_, newCount) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(RunningJobsIndicatorComponent, { handleClick: props.onClick, runningJobs: newCount }))));
}


/***/ }),

/***/ "./lib/context.js":
/*!************************!*\
  !*** ./lib/context.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);


// Context to be overridden with JupyterLab context
const TranslatorContext = react__WEBPACK_IMPORTED_MODULE_1___default().createContext(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__.nullTranslator);
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (TranslatorContext);


/***/ }),

/***/ "./lib/create-job-form.js":
/*!********************************!*\
  !*** ./lib/create-job-form.js ***!
  \********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CreateJobForm": () => (/* binding */ CreateJobForm)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _components_environment_picker__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./components/environment-picker */ "./lib/components/environment-picker.js");
/* harmony import */ var _components_output_format_picker__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./components/output-format-picker */ "./lib/components/output-format-picker.js");
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");
/* harmony import */ var _hooks__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./hooks */ "./lib/hooks.js");







function CreateJobForm(props) {
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_3__.useTranslator)('jupyterlab');
    const [state, setState] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)({
        jobName: '',
        inputFile: '',
        outputPath: '',
        environment: '',
        parameters: [],
        outputFormats: []
    });
    (0,react__WEBPACK_IMPORTED_MODULE_2__.useEffect)(() => {
        if (props.initialState) {
            setState(prevState => (Object.assign({}, props.initialState)));
        }
    }, [props.initialState]);
    const handleInputChange = (event) => {
        const target = event.target;
        const parameterNameMatch = target.name.match(/^parameter-(\d+)-name$/);
        const parameterValueMatch = target.name.match(/^parameter-(\d+)-value$/);
        if (parameterNameMatch !== null) {
            const idx = parseInt(parameterNameMatch[1]);
            // Update the parameters
            const newParams = state.parameters || [];
            newParams[idx].name = target.value;
            setState(Object.assign(Object.assign({}, state), { parameters: newParams }));
        }
        else if (parameterValueMatch !== null) {
            const idx = parseInt(parameterValueMatch[1]);
            // Update the parameters
            const newParams = state.parameters || [];
            newParams[idx].value = target.value;
            setState(prevState => (Object.assign(Object.assign({}, prevState), { parameters: newParams })));
        }
        else {
            const value = target.type === 'checkbox' ? target.checked : target.value;
            const name = target.name;
            setState(prevState => (Object.assign(Object.assign({}, prevState), { [name]: value })));
        }
    };
    const handleOutputFormatsChange = (event) => {
        const outputFormatsList = (0,_components_output_format_picker__WEBPACK_IMPORTED_MODULE_4__.outputFormatsForEnvironment)(state.environment);
        if (outputFormatsList === null) {
            return; // No data about output formats; give up
        }
        const formatName = event.target.value;
        const isChecked = event.target.checked;
        const wasChecked = state.outputFormats
            ? state.outputFormats.some(of => of.name === formatName)
            : false;
        const oldOutputFormats = state.outputFormats || [];
        // Go from unchecked to checked
        if (isChecked && !wasChecked) {
            // Get the output format matching the given name
            const newFormat = outputFormatsList.find(of => of.name === formatName);
            if (newFormat) {
                setState(Object.assign(Object.assign({}, state), { outputFormats: [...oldOutputFormats, newFormat] }));
            }
        }
        // Go from checked to unchecked
        else if (!isChecked && wasChecked) {
            setState(Object.assign(Object.assign({}, state), { outputFormats: oldOutputFormats.filter(of => of.name !== formatName) }));
        }
        // If no change in checkedness, don't do anything
    };
    const submitCreateJobRequest = async (event) => {
        const api = new _handler__WEBPACK_IMPORTED_MODULE_5__.SchedulerService({});
        // Serialize parameters as an object.
        let jobOptions = {
            name: state.jobName,
            input_uri: state.inputFile,
            output_prefix: state.outputPath,
            runtime_environment_name: state.environment
        };
        if (state.parameters !== undefined) {
            let jobParameters = {};
            state.parameters.forEach(param => {
                const { name, value } = param;
                if (jobParameters.hasOwnProperty(name)) {
                    console.error('Parameter ' +
                        name +
                        ' already set to ' +
                        jobParameters[name] +
                        ' and is about to be set again to ' +
                        value);
                }
                else {
                    jobParameters[name] = value;
                }
            });
            jobOptions.parameters = jobParameters;
        }
        if (state.outputFormats !== undefined) {
            jobOptions.output_formats = state.outputFormats.map(entry => entry.name);
        }
        api.createJob(jobOptions).then(response => {
            props.postCreateJob();
        });
    };
    const removeParameter = (idx) => {
        const newParams = state.parameters || [];
        newParams.splice(idx, 1);
        setState(Object.assign(Object.assign({}, state), { parameters: newParams }));
    };
    const addParameter = () => {
        const newParams = state.parameters || [];
        newParams.push({ name: '', value: '' });
        setState(Object.assign(Object.assign({}, state), { parameters: newParams }));
    };
    const api = new _handler__WEBPACK_IMPORTED_MODULE_5__.SchedulerService({});
    const environmentsPromise = async () => {
        const environmentsCache = sessionStorage.getItem('environments');
        if (environmentsCache !== null) {
            return JSON.parse(environmentsCache);
        }
        return api.getRuntimeEnvironments().then(envs => {
            sessionStorage.setItem('environments', JSON.stringify(envs));
            return envs;
        });
    };
    const nameInputName = 'jobName';
    const inputFileInputName = 'inputFile';
    const outputPathInputName = 'outputPath';
    const environmentInputName = 'environment';
    const outputFormatInputName = 'outputFormat';
    const formPrefix = 'jp-create-job-';
    const formRow = `${formPrefix}row`;
    const formLabel = `${formPrefix}label`;
    const formInput = `${formPrefix}input`;
    return (react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: `${formPrefix}form-container` },
        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("form", { className: `${formPrefix}form`, onSubmit: e => e.preventDefault() },
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: formRow },
                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("label", { className: formLabel, htmlFor: `${formPrefix}${nameInputName}` }, trans.__('Job name')),
                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("input", { type: "text", className: formInput, name: nameInputName, id: `${formPrefix}${nameInputName}`, value: state.jobName, onChange: handleInputChange })),
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: formRow },
                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("label", { className: formLabel, htmlFor: `${formPrefix}${inputFileInputName}` }, trans.__('Input file')),
                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("input", { type: "text", className: formInput, name: inputFileInputName, id: `${formPrefix}${inputFileInputName}`, value: state.inputFile, onChange: handleInputChange })),
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: formRow },
                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("label", { className: formLabel, htmlFor: `${formPrefix}${outputPathInputName}` }, trans.__('Output prefix')),
                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("input", { type: "text", className: formInput, name: outputPathInputName, id: `${formPrefix}${outputPathInputName}`, value: state.outputPath, onChange: handleInputChange })),
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: formRow },
                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("label", { className: formLabel, htmlFor: `${formPrefix}${environmentInputName}` }, trans.__('Environment')),
                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: formInput },
                    react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_components_environment_picker__WEBPACK_IMPORTED_MODULE_6__.EnvironmentPicker, { name: environmentInputName, id: `${formPrefix}${environmentInputName}`, onChange: handleInputChange, environmentsPromise: environmentsPromise(), initialValue: state.environment }))),
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_components_output_format_picker__WEBPACK_IMPORTED_MODULE_4__.OutputFormatPicker, { name: outputFormatInputName, id: `${formPrefix}${outputFormatInputName}`, onChange: handleOutputFormatsChange, environment: state.environment, value: state.outputFormats || [], rowClassName: formRow, labelClassName: formLabel, inputClassName: formInput }),
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: formRow },
                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("label", { className: formLabel }, trans.__('Parameters')),
                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: formInput },
                    state.parameters &&
                        state.parameters.map((param, idx) => (react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { key: idx, className: `${formPrefix}parameter-row` },
                            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("input", { name: `parameter-${idx}-name`, size: 15, value: param.name, type: "text", placeholder: trans.__('Name'), onChange: handleInputChange }),
                            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("input", { name: `parameter-${idx}-value`, size: 15, value: param.value, type: "text", placeholder: trans.__('Value'), onChange: handleInputChange }),
                            react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ToolbarButtonComponent, { className: `${formPrefix}inline-button`, icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.closeIcon, onClick: () => {
                                    removeParameter(idx);
                                    return false;
                                }, tooltip: trans.__('Delete this parameter') })))),
                    react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.Button, { minimal: true, onClick: (e) => {
                            addParameter();
                            return false;
                        }, title: trans.__('Add new parameter') },
                        react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.LabIcon.resolveReact, { icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.addIcon, tag: "span" })))),
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: formRow },
                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: formLabel }, "\u00A0"),
                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: `${formInput} ${formPrefix}submit-container` },
                    react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.Button, { type: "button", className: "jp-Dialog-button jp-mod-styled", onClick: props.cancelClick }, trans.__('Cancel')),
                    react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.Button, { type: "submit", className: "jp-Dialog-button jp-mod-accept jp-mod-styled", onClick: (e) => {
                            submitCreateJobRequest(e);
                            return false;
                        } }, trans.__('Run Job')))))));
}


/***/ }),

/***/ "./lib/handler.js":
/*!************************!*\
  !*** ./lib/handler.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Scheduler": () => (/* binding */ Scheduler),
/* harmony export */   "SchedulerService": () => (/* binding */ SchedulerService)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);


const API_NAMESPACE = 'scheduler';
class SchedulerService {
    constructor(options) {
        this.serverSettings =
            options.serverSettings || _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    }
    async getJobDefinitions(definition_id) {
        let data;
        let query = '';
        if (definition_id) {
            query = `/${definition_id}`;
        }
        try {
            data = await requestAPI(this.serverSettings, `job_definitions${query}`, {
                method: 'GET'
            });
        }
        catch (e) {
            console.error(e);
        }
        return data;
    }
    async createJobDefinition(definition) {
        let data;
        try {
            data = await requestAPI(this.serverSettings, 'job_definitions', {
                method: 'POST',
                body: JSON.stringify(definition)
            });
        }
        catch (e) {
            console.error(e);
        }
        return data;
    }
    async getJobs(jobQuery, job_id) {
        let data;
        let query = '';
        if (job_id) {
            query = `/${job_id}`;
        }
        else if (jobQuery) {
            query =
                '?' +
                    Object.keys(jobQuery)
                        .map(prop => {
                        if (prop === 'sort_by') {
                            if (jobQuery[prop] === undefined) {
                                return null;
                            }
                            // Serialize sort_by as a series of parameters in the firm dir(name)
                            // where 'dir' is the direction and 'name' the sort field
                            return jobQuery[prop].map(sort => `sort_by=${encodeURIComponent(sort.direction)}(${encodeURIComponent(sort.name)})`).join('&');
                        }
                        //@ts-ignore
                        const value = jobQuery[prop];
                        return `${encodeURIComponent(prop)}=${encodeURIComponent(value)}`;
                    })
                        .join('&');
        }
        try {
            data = await requestAPI(this.serverSettings, `jobs${query}`, {
                method: 'GET'
            });
        }
        catch (e) {
            console.error(e);
        }
        return data;
    }
    async getJobsCount(status) {
        let data = { count: 0 }; // Fail safe
        let query = '';
        if (status) {
            query = `?status=${encodeURIComponent(status)}`;
        }
        try {
            data = await requestAPI(this.serverSettings, `jobs/count${query}`, {
                method: 'GET'
            });
        }
        catch (e) {
            console.error(e);
        }
        return data.count;
    }
    async createJob(model) {
        let data;
        try {
            data = await requestAPI(this.serverSettings, 'jobs', {
                method: 'POST',
                body: JSON.stringify(model)
            });
        }
        catch (e) {
            console.error(e);
        }
        return data;
    }
    async setJobStatus(job_id, status) {
        let data;
        try {
            data = await requestAPI(this.serverSettings, `jobs/${job_id}`, {
                method: 'PATCH',
                body: JSON.stringify({ status })
            });
        }
        catch (e) {
            console.error(e);
        }
        return data;
    }
    async getRuntimeEnvironments() {
        let data;
        try {
            data = await requestAPI(this.serverSettings, 'runtime_environments', {
                method: 'GET'
            });
        }
        catch (e) {
            console.error(e);
        }
        return data;
    }
    async deleteJob(job_id) {
        try {
            await requestAPI(this.serverSettings, `jobs/${job_id}`, {
                method: 'DELETE'
            });
        }
        catch (e) {
            console.error(e);
        }
    }
}
/**
 * Call the API extension
 *
 * @param endPoint API REST end point for the extension
 * @param init Initial values for the request
 * @param expectData Is response data expected
 * @returns The response body interpreted as JSON
 */
async function requestAPI(settings, endPoint = '', init = {}, expectData = true) {
    // Make request to Jupyter API
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, API_NAMESPACE, endPoint);
    let response;
    try {
        response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeRequest(requestUrl, init, settings);
    }
    catch (error) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.NetworkError(error);
    }
    let data = await response.text();
    if (expectData && data.length > 0) {
        try {
            data = JSON.parse(data);
        }
        catch (error) {
            console.error('Not a JSON response body.', response);
        }
    }
    if (!response.ok) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.ResponseError(response, data.message || data);
    }
    return data;
}
var Scheduler;
(function (Scheduler) {
    let SortDirection;
    (function (SortDirection) {
        SortDirection["ASC"] = "asc";
        SortDirection["DESC"] = "desc";
    })(SortDirection = Scheduler.SortDirection || (Scheduler.SortDirection = {}));
})(Scheduler || (Scheduler = {}));


/***/ }),

/***/ "./lib/hooks.js":
/*!**********************!*\
  !*** ./lib/hooks.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "useTranslator": () => (/* binding */ useTranslator)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _context__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./context */ "./lib/context.js");


const useTranslator = (bundleId) => {
    const translator = (0,react__WEBPACK_IMPORTED_MODULE_0__.useContext)(_context__WEBPACK_IMPORTED_MODULE_1__["default"]);
    return translator.load(bundleId);
};


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "NotebookJobsPanelId": () => (/* binding */ NotebookJobsPanelId),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/filebrowser */ "webpack/sharing/consume/default/@jupyterlab/filebrowser");
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/launcher */ "webpack/sharing/consume/default/@jupyterlab/launcher");
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/statusbar */ "webpack/sharing/consume/default/@jupyterlab/statusbar");
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _lumino_polling__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @lumino/polling */ "webpack/sharing/consume/default/@lumino/polling/@lumino/polling");
/* harmony import */ var _lumino_polling__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_lumino_polling__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var _components_running_jobs_indicator__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! ./components/running-jobs-indicator */ "./lib/components/running-jobs-indicator.js");
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");
/* harmony import */ var _model__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./model */ "./lib/model.js");
/* harmony import */ var _notebook_jobs_panel__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ./notebook-jobs-panel */ "./lib/notebook-jobs-panel.js");
/* harmony import */ var _components_icons__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! ./components/icons */ "./lib/components/icons.js");














var CommandIDs;
(function (CommandIDs) {
    CommandIDs.deleteJob = 'scheduling:delete-job';
    CommandIDs.runNotebook = 'scheduling:run-notebook';
    CommandIDs.showNotebookJobs = 'scheduling:show-notebook-jobs';
    CommandIDs.stopJob = 'scheduling:stop-job';
})(CommandIDs || (CommandIDs = {}));
const NotebookJobsPanelId = 'notebook-jobs-panel';
/**
 * Initialization data for the jupyterlab-scheduler extension.
 */
const plugin = {
    id: 'jupyterlab-scheduler:plugin',
    requires: [_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_3__.IFileBrowserFactory, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__.ITranslator, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_1__.ILayoutRestorer],
    optional: [_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_5__.IStatusBar, _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_4__.ILauncher],
    autoStart: true,
    activate: activatePlugin
};
function getSelectedItem(widget) {
    if (widget === null) {
        return null;
    }
    // Get the first selected item.
    const firstItem = widget.selectedItems().next();
    if (firstItem === null || firstItem === undefined) {
        return null;
    }
    return firstItem;
}
function getSelectedFilePath(widget) {
    const selectedItem = getSelectedItem(widget);
    if (selectedItem === null) {
        return null;
    }
    return selectedItem.path;
}
function getSelectedFileName(widget) {
    const selectedItem = getSelectedItem(widget);
    if (selectedItem === null) {
        return null;
    }
    return selectedItem.name;
}
let scheduledJobsListingModel = null;
async function getNotebookJobsListingModel() {
    if (scheduledJobsListingModel) {
        return scheduledJobsListingModel;
    }
    const api = new _handler__WEBPACK_IMPORTED_MODULE_9__.SchedulerService({});
    const jobsResponse = await api.getJobs({});
    scheduledJobsListingModel = new _model__WEBPACK_IMPORTED_MODULE_10__.NotebookJobsListingModel(jobsResponse.jobs);
    return scheduledJobsListingModel;
}
async function activatePlugin(app, browserFactory, translator, restorer, statusBar, launcher) {
    const { commands } = app;
    const trans = translator.load('jupyterlab');
    const { tracker } = browserFactory;
    const api = new _handler__WEBPACK_IMPORTED_MODULE_9__.SchedulerService({});
    let mainAreaWidget;
    let widgetTracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.WidgetTracker({
        namespace: 'jupyterlab-scheduler'
    });
    restorer.restore(widgetTracker, {
        command: CommandIDs.showNotebookJobs,
        name: () => 'jupyterlab-scheduler'
    });
    const model = await getNotebookJobsListingModel();
    const jobsPanel = new _notebook_jobs_panel__WEBPACK_IMPORTED_MODULE_11__.NotebookJobsPanel({
        app,
        model,
        updateCreateJobFormSignal: _signal,
        translator
    });
    jobsPanel.title.icon = _components_icons__WEBPACK_IMPORTED_MODULE_12__.calendarMonthIcon;
    jobsPanel.title.caption = trans.__('Notebook Jobs');
    jobsPanel.node.setAttribute('role', 'region');
    jobsPanel.node.setAttribute('aria-label', trans.__('Notebook Jobs'));
    commands.addCommand(CommandIDs.deleteJob, {
        execute: async (args) => {
            const id = args['id'];
            await api.deleteJob(id);
        },
        // TODO: Use args to name command dynamically
        label: trans.__('Delete Job')
    });
    const showJobsPane = async (view) => {
        if (!mainAreaWidget || mainAreaWidget.isDisposed) {
            // Create a new widget
            mainAreaWidget = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.MainAreaWidget({
                content: jobsPanel
            });
            mainAreaWidget.content.view = view;
            mainAreaWidget.id = NotebookJobsPanelId;
            mainAreaWidget.title.icon = _components_icons__WEBPACK_IMPORTED_MODULE_12__.calendarMonthIcon;
            mainAreaWidget.title.label = trans.__('Notebook Jobs');
            mainAreaWidget.title.closable = true;
        }
        if (!widgetTracker.has(mainAreaWidget)) {
            // Track the state of the widget for later restoration
            widgetTracker.add(mainAreaWidget);
        }
        if (!mainAreaWidget.isAttached) {
            app.shell.add(mainAreaWidget, 'main');
        }
        mainAreaWidget.content.view = view;
        mainAreaWidget.content.update();
        app.shell.activateById(mainAreaWidget.id);
    };
    commands.addCommand(CommandIDs.showNotebookJobs, {
        execute: async () => showJobsPane('JobsList'),
        label: trans.__('Show Notebook Jobs'),
        icon: _components_icons__WEBPACK_IMPORTED_MODULE_12__.eventNoteIcon
    });
    commands.addCommand(CommandIDs.runNotebook, {
        execute: async () => {
            var _a, _b;
            await showJobsPane('CreateJobForm');
            const widget = tracker.currentWidget;
            const filePath = (_a = getSelectedFilePath(widget)) !== null && _a !== void 0 ? _a : '';
            const fileName = (_b = getSelectedFileName(widget)) !== null && _b !== void 0 ? _b : '';
            // Update the job form inside the notebook jobs widget
            const newState = {
                inputFile: filePath,
                jobName: fileName,
                outputPath: '',
                environment: ''
            };
            _signal.emit(newState);
        },
        label: trans.__('Create Notebook Job'),
        icon: _components_icons__WEBPACK_IMPORTED_MODULE_12__.calendarAddOnIcon
    });
    commands.addCommand(CommandIDs.stopJob, {
        execute: async (args) => {
            const id = args['id'];
            await api.setJobStatus(id, 'STOPPED');
        },
        // TODO: Use args to name command dynamically
        label: trans.__('Stop Job')
    });
    if (!statusBar) {
        // Automatically disable if statusbar missing
        return;
    }
    statusBar.registerStatusItem('jupyterlab-scheduler:status', {
        align: 'middle',
        item: _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.ReactWidget.create(react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_running_jobs_indicator__WEBPACK_IMPORTED_MODULE_13__.RunningJobsIndicator, { onClick: async () => showJobsPane('JobsList'), model: model }))
    });
    const statusPoll = new _lumino_polling__WEBPACK_IMPORTED_MODULE_7__.Poll({
        factory: async () => {
            const jobCount = await api.getJobsCount('IN_PROGRESS');
            model.updateJobsCount(jobCount);
        },
        frequency: { interval: 1000, backoff: false }
    });
    statusPoll.start();
    // Add to launcher
    if (launcher) {
        launcher.add({
            command: CommandIDs.showNotebookJobs
        });
    }
    console.log('JupyterLab extension jupyterlab-scheduler is activated!');
}
let _signal = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_8__.Signal(plugin);
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ }),

/***/ "./lib/model.js":
/*!**********************!*\
  !*** ./lib/model.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "NotebookJobsListingModel": () => (/* binding */ NotebookJobsListingModel)
/* harmony export */ });
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_0__);

class NotebookJobsListingModel {
    constructor(scheduled_jobs, next_token) {
        const inProgressJobs = scheduled_jobs
            ? scheduled_jobs.filter(job => job.status === 'IN_PROGRESS')
            : [];
        this.inProgressJobCount = inProgressJobs.length;
        this._scheduled_jobs = scheduled_jobs;
        this.scheduledJobsChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__.Signal(this);
        this.inProgressJobCountChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__.Signal(this);
    }
    updateJobs(jobs) {
        let jobsChanged = false;
        if (jobs.length != this._scheduled_jobs.length) {
            jobsChanged = true;
        }
        if (!jobsChanged) {
            for (let i = 0; i < jobs.length; i++) {
                const job = jobs[i];
                const modelJob = this._scheduled_jobs[i];
                if (job.status !== modelJob.status) {
                    jobsChanged = true;
                    break;
                }
            }
        }
        if (jobsChanged) {
            this._scheduled_jobs = jobs;
            this.scheduledJobsChanged.emit(jobs);
        }
    }
    updateJobsCount(jobCount) {
        if (jobCount !== this.inProgressJobCount) {
            this.inProgressJobCount = jobCount;
            this.inProgressJobCountChanged.emit(jobCount);
        }
    }
}


/***/ }),

/***/ "./lib/notebook-jobs-panel.js":
/*!************************************!*\
  !*** ./lib/notebook-jobs-panel.js ***!
  \************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "NotebookJobsPanel": () => (/* binding */ NotebookJobsPanel)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _context__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./context */ "./lib/context.js");
/* harmony import */ var _create_job_form__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./create-job-form */ "./lib/create-job-form.js");
/* harmony import */ var _components_notebook_jobs_list__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./components/notebook-jobs-list */ "./lib/components/notebook-jobs-list.js");
/* harmony import */ var _components_notebook_jobs_navigation__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./components/notebook-jobs-navigation */ "./lib/components/notebook-jobs-navigation.js");






class NotebookJobsPanel extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ReactWidget {
    constructor(options) {
        var _a, _b;
        super();
        this.addClass('jp-notebook-jobs-panel');
        const trans = options.translator.load('jupyterlab');
        this._title = (_a = options.title) !== null && _a !== void 0 ? _a : trans.__('Notebook Jobs');
        this._description = (_b = options.description) !== null && _b !== void 0 ? _b : trans.__('Job Runs');
        this._app = options.app;
        this._model = options.model;
        this._signal = options.updateCreateJobFormSignal;
        this._translator = options.translator;
        this._view = options.initialView || 'CreateJobForm';
    }
    set view(value) {
        this._view = value;
        this.update();
    }
    get createJobFormSignal() {
        return this._signal;
    }
    toggleView() {
        this.view = this._view === 'JobsList' ? 'CreateJobForm' : 'JobsList';
    }
    render() {
        return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_context__WEBPACK_IMPORTED_MODULE_2__["default"].Provider, { value: this._translator },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_notebook_jobs_navigation__WEBPACK_IMPORTED_MODULE_3__.NotebookJobsNavigation, { currentView: this._view, toggleSignal: this._signal, toggleFunction: () => this.toggleView() }),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { id: "jp-create-job-form-container", style: { display: this._view === 'CreateJobForm' ? 'block' : 'none' } },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.UseSignal, { signal: this._signal }, (_, newState) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_create_job_form__WEBPACK_IMPORTED_MODULE_4__.CreateJobForm, { initialState: newState, cancelClick: () => this.toggleView(), postCreateJob: () => this.toggleView() })))),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "jp-notebook-jobs-list-container", style: { display: this._view === 'JobsList' ? 'block' : 'none' } },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_notebook_jobs_list__WEBPACK_IMPORTED_MODULE_5__.NotebookJobsList, { app: this._app, createJobFormSignal: this._signal, showCreateJob: () => this.toggleView() }))));
    }
}


/***/ }),

/***/ "./style/icons/calendar-add-on.svg":
/*!*****************************************!*\
  !*** ./style/icons/calendar-add-on.svg ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 20 20\" height=\"16px\" width=\"16px\">\n  <path class=\"jp-icon3\" fill=\"#616161\" d=\"M10 15.833H4.25q-.729 0-1.24-.51-.51-.511-.51-1.24v-9q0-.729.51-1.239.511-.511 1.24-.511H5V1.667h1.75v1.666h4.833V1.667h1.75v1.666h.75q.729 0 1.24.511.51.51.51 1.239v4.959q-.229-.042-.437-.063-.208-.021-.438-.021-.229 0-.437.021-.209.021-.438.063V7.583H4.25v6.5H10q-.042.229-.062.438-.021.208-.021.437 0 .23.021.438.02.208.062.437Zm4.083 2.5v-2.5h-2.5v-1.75h2.5v-2.5h1.75v2.5h2.5v1.75h-2.5v2.5Z\"/>\n</svg>\n");

/***/ }),

/***/ "./style/icons/calendar-month.svg":
/*!****************************************!*\
  !*** ./style/icons/calendar-month.svg ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 18 18\" height=\"16px\" width=\"16px\">\n  <path class=\"jp-icon3\" fill=\"#616161\" d=\"M10 12q-.312 0-.531-.219-.219-.219-.219-.531 0-.312.219-.531.219-.219.531-.219.312 0 .531.219.219.219.219.531 0 .312-.219.531Q10.312 12 10 12Zm-3.25 0q-.312 0-.531-.219Q6 11.562 6 11.25q0-.312.219-.531.219-.219.531-.219.312 0 .531.219.219.219.219.531 0 .312-.219.531Q7.062 12 6.75 12Zm6.5 0q-.312 0-.531-.219-.219-.219-.219-.531 0-.312.219-.531.219-.219.531-.219.312 0 .531.219.219.219.219.531 0 .312-.219.531-.219.219-.531.219ZM10 15q-.312 0-.531-.219-.219-.219-.219-.531 0-.312.219-.531.219-.219.531-.219.312 0 .531.219.219.219.219.531 0 .312-.219.531Q10.312 15 10 15Zm-3.25 0q-.312 0-.531-.219Q6 14.562 6 14.25q0-.312.219-.531.219-.219.531-.219.312 0 .531.219.219.219.219.531 0 .312-.219.531Q7.062 15 6.75 15Zm6.5 0q-.312 0-.531-.219-.219-.219-.219-.531 0-.312.219-.531.219-.219.531-.219.312 0 .531.219.219.219.219.531 0 .312-.219.531-.219.219-.531.219ZM4.5 18q-.625 0-1.062-.448Q3 17.104 3 16.5v-11q0-.604.438-1.052Q3.875 4 4.5 4H6V2h1.5v2h5V2H14v2h1.5q.625 0 1.062.448Q17 4.896 17 5.5v11q0 .604-.438 1.052Q16.125 18 15.5 18Zm0-1.5h11V9h-11v7.5Z\"/>\n</svg>\n");

/***/ }),

/***/ "./style/icons/event-note.svg":
/*!************************************!*\
  !*** ./style/icons/event-note.svg ***!
  \************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"48\" width=\"48\">\n  <path class=\"jp-icon3\" fill=\"#616161\" d=\"M14 27v-3h20v3Zm0 9v-3h13.95v3Zm-5 8q-1.2 0-2.1-.9Q6 42.2 6 41V10q0-1.2.9-2.1Q7.8 7 9 7h3.25V4h3.25v3h17V4h3.25v3H39q1.2 0 2.1.9.9.9.9 2.1v31q0 1.2-.9 2.1-.9.9-2.1.9Zm0-3h30V19.5H9V41Z\"/>\n</svg>\n");

/***/ }),

/***/ "./style/icons/replay.svg":
/*!********************************!*\
  !*** ./style/icons/replay.svg ***!
  \********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 22 22\" height=\"16px\" width=\"16px\">\n  <path class=\"jp-icon3\" fill=\"#616161\" d=\"M10 18.125q-1.458 0-2.729-.552-1.271-.552-2.219-1.5t-1.5-2.219Q3 12.583 3 11.125h1.5q0 2.271 1.615 3.885Q7.729 16.625 10 16.625t3.885-1.615q1.615-1.614 1.615-3.885T13.885 7.24Q12.271 5.625 10 5.625h-.125l1.063 1.063L9.875 7.75 7 4.875 9.875 2l1.063 1.062-1.084 1.063H10q1.458 0 2.729.552 1.271.552 2.219 1.5t1.5 2.219Q17 9.667 17 11.125q0 1.458-.552 2.729-.552 1.271-1.5 2.219t-2.219 1.5q-1.271.552-2.729.552Z\"/>\n</svg>\n");

/***/ })

}]);
//# sourceMappingURL=lib_index_js.a618e07625363d3adeb4.js.map