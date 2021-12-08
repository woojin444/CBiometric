import React from "react";
var style = {
  position: "relative",
  bottom: "0",
  width: "100%"
};

export default () => {
  return (
    <div>
      <div style={style}>
        <footer className="bg-dark text-white mt-5 p-4 text-center">
          Copyright &copy; {new Date().getFullYear()} Biometix Face Miner
        </footer>
      </div>
    </div>
  );
};
