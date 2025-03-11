
cy.visit('https://mrjindev.com/?m=login&t=phone&returnUrl=%2Fgame%2F101765');

cy.get('.css-olqel7-indicatorContainer svg').click();

cy.get('#\\3Arc\\3A').click();
cy.get('#\\3Arc\\3A').type('armenia');


cy.get('#phoneNumber').click().type('99018082');

cy.get('#password').click().clear();


cy.get('.css-466zim').click();


cy.url().should('contain', 'https://mrjindev.com/api/identity/connect/authorize');
cy.url().should('contain', 'https://mrjindev.com/game/101765');

cy.get('.css-jkx7gx path').click();
cy.url().should('contain', 'https://predictor-frontend-stage-branch-fpbcfgbjccfdd7db.westus-01.azurewebsites.net/');

cy.get('.user-id').should('have.text', '18019612');