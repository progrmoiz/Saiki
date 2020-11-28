import React, { useCallback } from 'react'
import ReactDOM from 'react-dom'
import Material from './Material'

export default class extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            materials: []
        }
    }

    componentWillReceiveProps(nextProps) {
        // You don't have to do this check first, but it can help prevent an unneeded render
        if (nextProps.materials !== this.state.materials) {
            this.setState({
                materials: nextProps.materials,
            });
        }
    }

    render() {
        return <ul className="material">
            {[...this.state.materials].reverse().map((m, id) => (
                <Material onRemoveClick={this.props.onRemoveClick} m={m} key={id} />
            ))}
        </ul>
    }
}