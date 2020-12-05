import React, { useCallback } from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'
import cx from 'classnames'
import {
  setChonkyDefaults,
  FileBrowser,
  FileContextMenu,
  FileList,
  FileHelper,
  FileNavbar,
  FileToolbar,
  ChonkyActions
} from 'chonky';
import { ChonkyIconFA } from 'chonky-icon-fontawesome';
import { useDropzone } from 'react-dropzone'

setChonkyDefaults({ iconComponent: ChonkyIconFA });

function MyDropZone(props) {
  const onDrop = useCallback(props.onDrop, [])
  const { acceptedFiles, getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop })

  return (
    <>
      <div className="dropzone dropzone-multiple mb-2" {...getRootProps()}>
        <input {...getInputProps()} />
        <div className="dz-default dz-message">
        {
          isDragActive ?
            <span>Drop the files here ...</span> :
            <span>Drag 'n' drop some files here, or click to select files</span>
        }
        </div>
      </div>
    </>
  )
}

class ResourcesApp extends React.Component {

  constructor(props) {
    super(props)
    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

    this.state = {}
  }

  handleOnDrop = acceptedFiles => acceptedFiles.forEach((f, id) => {
    const fileMap = this.state.fileMap;
    const currentFolderId = this.state.currentFolderId;
    const currentFolder = fileMap[currentFolderId];

    const formData = new FormData();
    formData.append('file', f);
    formData.append('folder', currentFolder.pk);
    formData.append('user', this.props.user);

    return axios.post(this.props.file_create_url, formData, {
      headers: { 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' },
    })
    .then(this.refreshStates) // bad choice
  })

  fetchCourses = (fn, error_fn) => axios.get(this.props.request_url).then(fn).catch(error_fn)

  getFiles = (fileMap, currentFolderId) => {
    const currentFolder = fileMap[currentFolderId]

    const files = currentFolder.childrenIds
      ? currentFolder.childrenIds.map(fileId => fileMap[fileId] ?? null)
      : [];

    return files;
  }

  getFolderChain = (fileMap, currentFolderId) => {
    const currentFolder = fileMap[currentFolderId];

    const folderChain = [currentFolder];

    let parentId = currentFolder.parentId;
    while (parentId) {
      const parentFile = fileMap[parentId];
      if (parentFile) {
        folderChain.unshift(parentFile);
        parentId = parentFile.parentId;
      } else {
        break;
      }
    }

    return folderChain;
  }

  componentDidMount() {
    this.fetchCourses((res) => {
      this.setState({
        fileMap: res.data.fileMap,
        currentFolderId: res.data.rootFolderId,
        files: this.getFiles(res.data.fileMap, res.data.rootFolderId),
        folderChain: this.getFolderChain(res.data.fileMap, res.data.rootFolderId)
      })
    })
  }

  fileActions = [ChonkyActions.CreateFolder, ChonkyActions.DeleteFiles]

  openInNewTab = (url) => {
    const newWindow = window.open(url, '_blank', 'noopener,noreferrer')
    if (newWindow) newWindow.opener = null
  }

  refreshStates = () => this.fetchCourses((res) => {
    this.setState({
      fileMap: res.data.fileMap,
      files: this.getFiles(res.data.fileMap, this.state.currentFolderId),
      folderChain: this.getFolderChain(res.data.fileMap, this.state.currentFolderId)
    })
  })

  moveFiles = (files, source, destination) => Promise.all(files.map(file => {
    const formData = new FormData();

    if (FileHelper.isDirectory(file)) {
      formData.append('name', file.name)
      formData.append('course_offering', this.props.course_offering)
      formData.append('parent', destination.pk)
      formData.append('user', file.user)
    } else {
      formData.append('folder', destination.pk)
      formData.append('user', file.user)
    }

    return axios.put(file.request_url, formData, {
      headers: { 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' }
    })
  })
  ).then(this.refreshStates);


  deleteFiles = (files) => {
    const newFileMap = { ...this.state.fileMap }
    if (!window.confirm('Are you sure you wish to delete this item?')) return

    files.map(file => {
      delete newFileMap[file.id]

      if (file.parentId) {
        const parent = newFileMap[file.parentId];
        const newChildrenIds = parent.childrenIds.filter(
          (id) => id !== file.id
        );
        newFileMap[file.parentId] = {
          ...parent,
          childrenIds: newChildrenIds,
          childrenCount: newChildrenIds.length,
        };
      }

      // probably not the best practice        
      return axios.delete(file.request_url);
    }
    )

    this.setState({
      fileMap: newFileMap,
      files: this.getFiles(newFileMap, this.state.currentFolderId),
      folderChain: this.getFolderChain(newFileMap, this.state.currentFolderId)
    })
  }

  createFolder = (folderName) => {
    const fileMap = this.state.fileMap;
    const currentFolderId = this.state.currentFolderId;
    const currentFolder = fileMap[currentFolderId];

    const formData = new FormData();
    formData.append('course_offering', this.props.course_offering); // 
    formData.append('name', folderName);
    formData.append('parent', currentFolder.pk)
    formData.append('user', this.props.user)

    // maybe a bit bad because we are refreshing the whole state
    return axios.post(this.props.folder_create_url, formData, {
      headers: { 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' }
    })
      .then(this.refreshStates);
  }

  handleFileAction = (data) => {
    if (data.id === ChonkyActions.OpenFiles.id) {
      const { targetFile, files } = data.payload;
      const fileToOpen = targetFile ?? files[0];
      if (fileToOpen && FileHelper.isDirectory(fileToOpen)) {
        this.setState({
          currentFolderId: fileToOpen.id,
          files: this.getFiles(this.state.fileMap, fileToOpen.id),
          folderChain: this.getFolderChain(this.state.fileMap, fileToOpen.id)
        });
        return;
      } else {
        this.openInNewTab(fileToOpen.url)
      }
    } else if (data.id === ChonkyActions.DeleteFiles.id) {
      this.deleteFiles(data.state.selectedFilesForAction);
    } else if (data.id === ChonkyActions.MoveFiles.id) {
      this.moveFiles(
        data.payload.files,
        data.payload.source,
        data.payload.destination
      );
    } else if (data.id === ChonkyActions.CreateFolder.id) {
      const folderName = prompt('Provide the name for your new folder:');
      if (folderName) this.createFolder(folderName);
    }
  }

  render() {
    return <>
      <MyDropZone onDrop={this.handleOnDrop} />
      <div style={{ height: 400 }}>
        <FileBrowser
          files={this.state.files}
          folderChain={this.state.folderChain}
          fileActions={this.fileActions}
          onFileAction={this.handleFileAction}
          defaultFileViewActionId={ChonkyActions.EnableListView.id}
        >
          <FileNavbar />
          <FileToolbar />
          <FileList />
          <FileContextMenu />
        </FileBrowser>
      </div>
    </>
  }
}

const element = React.createElement(ResourcesApp, window.resources_list_app_props);
ReactDOM.render(
  element,
  document.getElementById('resources-app')
);