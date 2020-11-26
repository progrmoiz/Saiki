import React, { useCallback } from 'react'
import ReactDOM from 'react-dom'
import { useDropzone } from 'react-dropzone'

export default function (props) {
    const onDrop = useCallback(props.onDrop, [])
    const { acceptedFiles, getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop })

    return (
        <>
            <div className="dropzone dropzone-multiple mb-2" {...getRootProps()}>
                <input {...getInputProps()} />
                {
                    isDragActive ?
                        <p>Drop the files here ...</p> :
                        <div className="dz-default dz-message">
                            <span>Drag 'n' drop some files here, or click to select files</span>
                        </div>
                }
            </div>
        </>
    )
}