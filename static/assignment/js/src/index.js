import React, { useCallback } from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'
import fileExtension from 'file-extension'
import cx from 'classnames'
import { basename } from 'path-browserify'
import { useDropzone } from 'react-dropzone'
import MaterialList from './MaterialList'
import Dropzone from './Dropzone'

class MaterialApp extends React.Component {
  constructor(props) {
    super(props)
    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

    this.state = {
      materials: [],
      uploadMaterials: []
    }
  }

  fetchMaterial = (fn) => axios.get(this.props.request_url).then(fn)

  componentDidMount() {
    this.fetchMaterial((materials) => {
      this.setState({ materials: materials.data })
    })
  }

  handleRemoveClick = (evt, material) => {
    evt.preventDefault()
    if (!window.confirm('Are you sure you wish to delete this item?')) return

    return axios.delete(material.request_url)
      .then(res => {
        this.setState({
          materials: this.state.materials.filter(m => m.id != material.id)
        })
      })
  }

  handleOnDrop = acceptedFiles => acceptedFiles.forEach((f, id) => {
    const formData = new FormData();
    formData.append('file', f);
    formData.append(this.props.page, this.props.page_id);

    this.setState({
      materials: [
        ...this.state.materials,
        { file: f.path, id: id, beingUpload: true }
      ]
    })

    return axios.post(this.props.request_url, formData, {
      headers: { 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' },
      onUploadProgress: (evt) => {
        const percentages = +((evt.loaded / evt.total) * 100).toFixed(2);
        console.log(percentages)
        window.unsavedChanges = true;
        debounce(() => {
          this.setState({
            materials: this.state.materials
              .map(m => (m.beingUpload && m.id == id) ? {
                ...m,
                progress: percentages
              } : m)
          })
          window.unsavedChanges = false;
        }, 500)()
      },
    })
      .then(res => {
        const { data, config: { url } } = res;
        data.request_url = `${url}${data.id}`

        this.setState({
          uploadMaterials: this.state.uploadMaterials.filter((m) => m.id != id),
          materials: this.state.materials
            .map(m => (m.beingUpload && m.id == id) ? {
              ...m,
              progress: false,
              beingUpload: false,
              ...data
            } : m)
        })
      }
      )

  }
  )

  render() {

    return <>
      {!this.props.graded && !this.props.turned ? <Dropzone onDrop={this.handleOnDrop} /> : ''}
      <MaterialList onRemoveClick={this.handleRemoveClick} materials={this.state.materials} />
    </>
  }
}

const element = React.createElement(MaterialApp, window.material_list_app_props);
ReactDOM.render(
  element,
  document.getElementById('material-app')
);