"use strict";

function debounce(callback, wait, immediate = false) {
	let timeout = null 
	
	return function() {
	const callNow = immediate && !timeout
	const next = () => callback.apply(this, arguments)
	
	clearTimeout(timeout)
	timeout = setTimeout(next, wait)

	if (callNow) {
		next()
	}
	}
}

window.addEventListener("beforeunload", function (e) {
	if (window.unsavedChanges) {
	e.returnValue = 'Unsaved Changes!';
	return 'Unsaved Changes!';
	};
	return;
});

var Dropzones = (function() {


	var $dropzone = $('[data-toggle="dropzone"]');
	var $dropzonePreview = $('.dz-preview');

	function init($this) {
		var multiple = ($this.data('dropzone-multiple') !== undefined) ? true : false;
		var preview = $this.find($dropzonePreview);
		var currentFile = undefined;
        var csrftoken = $this.find('[name="csrfmiddlewaretoken"]').val();

		// Init options
		var options = {
			url: $this.data('dropzone-url'),
			thumbnailWidth: null,
			thumbnailHeight: null,
			previewsContainer: preview.get(0),
			previewTemplate: preview.html(),
			maxFiles: (!multiple) ? 1 : null,
            // autoProcessQueue: false,
            headers: {
                'X-CSRFToken': csrftoken
            },
			acceptedFiles: (!multiple) ? 'image/*' : null,
			init: function() {
				this.on("addedfile", function(file) {
					if (!multiple && currentFile) {
						this.removeFile(currentFile);
					}
					currentFile = file;
				})
			},
			uploadprogress: function(file, progress, bytesSent) {
   				window.unsavedChanges = true;
				debounce(function() {
					if (file.previewElement) {
							var progressElement = file.previewElement.querySelector("[data-dz-uploadprogress]");
							progressElement.style.width = Math.trunc(progress) + "%";
							// progressElement.querySelector(".progress-text").textContent = Math.trunc(progress) + "%";
							if (progress == 100) {
									$(file.previewElement.querySelector(".progress")).fadeOut(1000)
							}
					}
					window.unsavedChanges = false;
				}, 500)()
			}
		}
		preview.html('');

		$this.dropzone(options)
	}

	function globalOptions() {
		Dropzone.autoDiscover = false;
	}

	if ($dropzone.length) {
		globalOptions();
		$dropzone.each(function() {
			init($(this));
		});
	}

})();

var QuillEditor = (function() {

	var $quill = $('[data-toggle="quill"]');
	if (!$('[data-toggle="quill"]').length) return

	var quill = new Quill($quill.get(0), {
	  modules: {
		toolbar: [
		  ['bold', 'italic'],
		  ['link'],
		  [{
			'list': 'ordered'
		  }, {
			'list': 'bullet'
		  }]
		]
	  },
	  theme: 'snow'
	});
	quill.root.innerHTML = $('.quill-initial-state').html()

	var syncHtml = debounce(function() {
	  var contents = $(".ql-editor").html();
	  $('#description').val(contents);
	  window.unsavedChanges = false;
	}, 500);
  
	quill.on('text-change', function() {
	  window.unsavedChanges = true;
	  syncHtml();
	});
  
  })();