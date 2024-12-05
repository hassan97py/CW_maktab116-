const nameInput = document.getElementById("name");
const salaryInput = document.getElementById("salary");
const saveBtn = document.getElementById("saveBtn");
const sortinput = document.getElementById("sort");
const deleteAllBtn = document.getElementById("deleteAll");
const listSalaries = document.getElementById("listSalaries");

const validateInput = (name, salary) => {
  const x = { validN: false, errorName: "نام باید بیشتر از 3 حرف باشد",validS:false, errorSalary: "حقوق باید بیشتر از 1000 تومن باشد" };
  if (name.length > 2) {
    x.validN = true;
    // x.errorName = "";
  } 
//   else {
//     // x.validN = false;
//     x.errorName = "نام باید بیشتر از 3 حرف باشد";
//   }
  if (salary >= 1000) {
    x.validS = true;
    // x.errorSalary = "";
  } 
//   else {
//     // x.validS = false;
//     x.errorSalary = "حقوق باید بیشتر از 1000 تومن باشد";
//   }
  return x;
};

const addSalary = () => {
  const nameValue = nameInput.value;
  const salaryValue = salaryInput.value;
  const validate = validateInput(nameValue, salaryValue);
  if (validate.validN && validate.validS) {
    console.log("ok");
  } else {
    console.log(!validate.validN && validate.errorName,!validate.validS && validate.errorSalary);
  }
};

saveBtn.addEventListener("click", addSalary);
