import { useState } from 'react';
import './PdfLoader.css'

function PdfLoader(){
    const saveFile = async (e) => {
        e.preventDefault()

        let files = e.target.files
        console.warn(files)
    }

    return(
        <div className="PdfLoader">
            <form id="upload">
                <label>Selecione um arquivo PDF</label>
                <input id="fileupload" type="file" name="fileupload" accept=".pdf" onChange={(e) => saveFile(e)}/>
            </form>
        </div>
    )
}

export default PdfLoader;