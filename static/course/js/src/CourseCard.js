import React from 'react'
import ReactDOM from 'react-dom';
import cx from 'classnames';
import Dropdown from 'react-bootstrap/Dropdown'

const CustomToggle = React.forwardRef(({ children, onClick, className }, ref) => (
    <a
      href="#"
      ref={ref}
      onClick={(e) => {
        e.preventDefault();
        onClick(e);
      }}
      className={ className }
    >
      {children}
      <i className="fas fa-ellipsis-h"></i>
    </a>
  ));

export function CourseCard(props) {
return (
    <div className="col-lg-3">
        <div className="card course-card" style={{background: props.color_bg}}>
            <div className="card-body">
                <h3 className={
                    cx("card-title", `text-${props.color_fg}`, "mb-3")
                }>{ props.description }</h3>
                <h5 className={
                    cx("card-text", `text-${props.color_fg}`, "mb-4")
                }>{ props.code } - { props.term }</h5>
                <div className="position-relative">
                    { props.course_url ? 
                        <a href={props.course_url} className={
                            cx("btn", "btn-sm", {
                                "btn-default": props.color_fg == "default",
                                "btn-secondary": props.color_fg != "default",
                            }) }>View Course</a>
                    : <a href='#' className={
                            cx("btn", "btn-sm", {
                                "btn-default": props.color_fg == "default",
                                "btn-secondary": props.color_fg != "default",
                            }) }>Get Invite</a> }
                    { props.request_url ? 
                    <Dropdown className={ cx("position-absolute", "right-0" )}>
                    <Dropdown.Toggle 
                        as={CustomToggle} 
                        className={ cx("p-1", "text-sm", `text-${props.color_fg}`) }
                    />
                    <Dropdown.Menu>
                        <Dropdown.Item onClick={(evt) => props.onHideClick(evt, props.request_url)}>{ !props.is_hidden ? 'Hide course' : 'Show course' }</Dropdown.Item>
                    </Dropdown.Menu>
                    </Dropdown>
                    : '' }
                </div>
            </div>
        </div>
    </div>
);
}
