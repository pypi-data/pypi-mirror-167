import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';
import { FileEditor, IEditorTracker } from '@jupyterlab/fileeditor';
import { INotebookTracker } from '@jupyterlab/notebook';
import { ICommandPalette } from '@jupyterlab/apputils';
import { ISettingRegistry } from '@jupyterlab/settingregistry';
import { Cell } from '@jupyterlab/cells';

import { CodeMirrorEditor, ICodeMirror } from '@jupyterlab/codemirror';
import CodeMirror from 'codemirror';

import * as _ from 'underscore';

class SqlCodeMirror {
  ignored_tokens: Set<string> = new Set();
  settings: ISettingRegistry.ISettings | undefined;
  accepted_types: string[] | undefined;
  constructor(
    protected app: JupyterFrontEnd,
    protected tracker: INotebookTracker,
    protected editor_tracker: IEditorTracker,
    protected setting_registry: ISettingRegistry,
    protected code_mirror: ICodeMirror,
    protected palette?: ICommandPalette | null
  ) {
    this.tracker.activeCellChanged.connect(() => {
      if (this.tracker.activeCell) {
        this.setup_cell_editor(this.tracker.activeCell);
      }
    });
    // setup newly open editors
    this.editor_tracker.widgetAdded.connect((sender, widget) =>
      this.setup_file_editor(widget.content, true)
    );
    // refresh already open editors when activated (because the MIME type might have changed)
    this.editor_tracker.currentChanged.connect((sender, widget) => {
      if (widget !== null) {
        this.setup_file_editor(widget.content, false);
      }
    });
  }

  refresh_state() {
    // update the active cell (if any)
    if (this.tracker.activeCell !== null) {
      this.setup_cell_editor(this.tracker.activeCell);
    }

    // update the current file editor (if any)
    if (this.editor_tracker.currentWidget !== null) {
      this.setup_file_editor(this.editor_tracker.currentWidget.content);
    }
  }

  setup_file_editor(file_editor: FileEditor, setup_signal = false): void {
    if (setup_signal) {
      file_editor.model.mimeTypeChanged.connect((model, args) => {
        // putting at the end of execution queue to allow the CodeMirror mode to be updated
        setTimeout(() => this.setup_file_editor(file_editor), 0);
      });
    }
  }

  setup_cell_editor(cell: Cell): void {
    if (cell !== null && cell.model.type === 'code') {
      const code_mirror_editor = cell.editor as CodeMirrorEditor;
      const debounced_on_change = _.debounce(() => {
        // check for editor with first line starting with %%sql
        const line = code_mirror_editor
          .getLine(code_mirror_editor.firstLine())
          ?.trim();
        if (line?.startsWith('%%sql')) {
          code_mirror_editor.editor.setOption('mode', 'text/x-sql');
        } else {
          code_mirror_editor.editor.setOption('mode', 'text/x-ipython');
        }
      }, 300);
      code_mirror_editor.editor.on('change', debounced_on_change);
      debounced_on_change();
    }
  }

  extract_editor(cell_or_editor: Cell | FileEditor): CodeMirror.Editor {
    const editor_temp = cell_or_editor.editor as CodeMirrorEditor;
    return editor_temp.editor;
  }
}

function activate(
  app: JupyterFrontEnd,
  tracker: INotebookTracker,
  editor_tracker: IEditorTracker,
  setting_registry: ISettingRegistry,
  code_mirror: ICodeMirror,
  palette: ICommandPalette | null
): void {
  new SqlCodeMirror(
    app,
    tracker,
    editor_tracker,
    setting_registry,
    code_mirror,
    palette
  );
  console.log('SQLCodeMirror loaded.');
}

/**
 * Initialization data for the jupyterlab_apod extension.
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: '@composable/jupyterlabs-sql-codemirror',
  autoStart: true,
  requires: [INotebookTracker, IEditorTracker, ISettingRegistry, ICodeMirror],
  optional: [ICommandPalette],
  activate: activate
};

export default extension;
