LATEX=latex --output-format=pdf -output-directory tmp_certificates

students:
	$(LATEX) students_certificate_changed
	$(LATEX) students_certificate_changed
	$(LATEX) students_certificate_changed

professors: 
	$(LATEX) professors_certificate_changed
	$(LATEX) professors_certificate_changed
	$(LATEX) professors_certificate_changed

organizers: 
	$(LATEX) organizers_certificate_changed
	$(LATEX) organizers_certificate_changed
	$(LATEX) organizers_certificate_changed

# local: 
# 	$(LATEX) local_certificate_changed
# 	$(LATEX) local_certificate_changed
# 	$(LATEX) local_certificate_changed

# logistic: 
# 	$(LATEX) logistic_certificate_changed
# 	$(LATEX) logistic_certificate_changed
# 	$(LATEX) logistic_certificate_changed



clean:
	rm -rfv *~
	cd tmp_certificates; rm -rfv *.log *.aux
