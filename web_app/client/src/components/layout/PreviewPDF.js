// import React, { Component } from "react";
// import { Document, Page } from "react-pdf";
// import result from "../../report/result.pdf";

// const options = {
//   cMapUrl: "cmaps/",
//   cMapPacked: true
// };

// class PreviewPDF extends Component {
//   state = {
//     file: result,
//     numPages: null
//   };
//   onDocumentLoad = ({ numPages }) => {
//     this.setState({ numPages });
//   };

//   render() {
//     const { pageNumber, numPages } = this.state;

//     return (
//       <div>
//         <Document
//           file={result}
//           onLoadSuccess={this.onDocumentLoad}
//           options={options}
//         >
//           {Array.from(new Array(numPages), (el, index) => (
//             <Page key={`page_${index + 1}`} pageNumber={index + 1} />
//           ))}
//         </Document>
//         <p>
//           Page {pageNumber} of {numPages}
//         </p>
//       </div>
//     );
//   }
// }

// export default PreviewPDF;
