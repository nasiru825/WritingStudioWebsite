using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.IO;


namespace Writing_Studio.Controllers
{
    public class FileUploadController : Controller
    {
        // GET: FileUpload
        public ActionResult Index()
        {
            return View();
        }
        [HttpPost]
        public ActionResult Index(HttpPostedFileBase file)
        {
           
            
                    if (file != null)
                    {
                        string FileName = Path.GetFileName(file.FileName);
                        string path = Server.MapPath("~/Content/Profile1.jpg");
                        file.SaveAs(path);
                    }
                    ViewBag.FileStatus = "File uploaded successfully.";
                
            
            
            return View("Index");
        }
    }
}