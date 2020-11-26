import React, { useCallback } from 'react'
import ReactDOM from 'react-dom'
import fileExtension from 'file-extension'
import { basename } from 'path-browserify'
import cx from 'classnames'

export default class extends React.Component {
    render() {
        const { m: material } = this.props;

        return (
            <li className="mb-2 position-relative">
                <a href={material.file} target="_blank" className="position-relative">
                    <span className={cx("fiv-sqo", `fiv-icon-${fileExtension(material.file)}`)}></span>
                    <span className="text-sm font-weight-bold text-dark">{basename(material.file)}</span>
                    <span onClick={(evt) => { this.props.onRemoveClick(evt, material) }} className="px-2 position-absolute right-0"><i className="ni ni-fat-remove"></i></span>
                </a>
                { material.progress ?
                    <div className="progress">
                        <div className="progress-bar bg-default" role="progressbar" style={{ 'width': `${material.progress}%` }}>
                        </div>
                    </div> : ''}
            </li>
        )
    }
}