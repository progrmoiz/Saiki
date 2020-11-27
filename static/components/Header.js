import React from 'react'
import ReactDOM from 'react-dom';

export default (props) =>
    <div className="header bg-primary pb-6">
        <div className="container-fluid">
            <div className="header-body">
                <div className="row align-items-center py-4">
                    <div className="col-lg-6">
                        <h3 className="h2 text-white d-inline-block mb-0">{props.heading}</h3>
                        {props.subheading ?
                            <h5 className="text-light">{props.subheading}</h5> : ''}
                    </div>
                </div>
            </div>
        </div>
    </div>
